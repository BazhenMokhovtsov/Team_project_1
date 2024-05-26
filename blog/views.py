from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, Comment, Category
from .forms import CommentForm, SortPostForm
from django.core.paginator import Paginator
from django.db.models import Q


def paginator_page(request, queryset, pages):
    paginator = Paginator(queryset,pages)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj
    
def sorting_by(request, queryset):
    # # if sort_by:
    # #     sort_by = request.session.get('sort') #тут находятся данные которые мы передаои в форму под ключем сорт Но в теории при первом посещении тут нету значения
    # # else:
    # #     request.session['sort'] = 'update_data'

    # # if request.session.get('sort') == None:
    # #     sort_by = 'update_data'
    # # почему если использовать request.session['sort']  выдаёт ошибку при первом переходе на стр. а при гет сорт нет ? в квадратных скобках мы пытаемся напрямую получить значение ключа. а в гет мы как-бы запрашиваем его.
    # # print(f'{sort_by} sort_by')

    sort_by = request.session.get('sort')

    if request.method == 'POST':
        sort_form = SortPostForm(request.POST)
        if sort_form.is_valid():
            sort_by = sort_form.cleaned_data['sort_by']
            request.session['sort'] = sort_by 
    else:
        sort_form = SortPostForm(initial={'sort_by': sort_by})

    if sort_by == 'update_date':
        queryset = queryset.order_by('update_date')
    elif sort_by == 'category':
        queryset = queryset.order_by('category_id')
    elif sort_by == 'title':
        queryset = queryset.order_by('title')
    else:
        queryset
        
    return queryset, sort_form

def show_all_categories(request):
    sorted_posts = Post.objects.filter(published=True)
    sorted_posts,sort_form = sorting_by(request, sorted_posts)

    page_obj = paginator_page(request, sorted_posts, 2)
    
    content = {
        'sort_form': sort_form,
        'page_obj': page_obj,
    }

    return render(request, 'blog/1st_page.html', content)


def show_posts_to_category(request, category_id):
    posts = Post.objects.filter(category__id=category_id, published=True)
    posts, sort_form = sorting_by(request,posts)

    posts = paginator_page(request,posts,2)

    content = {

        "posts": posts,
        "sort_form": sort_form,
    }

    return render(request, 'blog/category_posts.html', content)


def show_single_post(request, post_id):
    single_post = Post.objects.get(pk=post_id)
    comments = Comment.objects.filter(post__id=post_id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.post = single_post
            post.author = request.user
            post.save()
        return redirect('blog:show_single_post', post_id=post_id)
    else:
        form = CommentForm()

    content = {
        "form": form,
        "single_post": single_post,
        "comments": comments,
    }

    return render(request, "blog/single_post.html", content)


def del_comment(request,comment_id):
    comment = Comment.objects.get(pk = comment_id)
    comment.delete()

    return redirect("blog:show_single_post", post_id=comment.post.pk)

#для поиска используется бибилиотека Q sql3
def search(request):
    if request.method == 'POST':
        userinput = request.POST.get('search')
        request.session['search_data'] = userinput
    else:
        userinput = request.session.get('search_data')

    query = Q(title__icontains=userinput) | Q(text__icontains=userinput)
    search_result = Post.objects.filter(query, published=True)

    search_result = paginator_page(request,search_result,1)  # Не работл...при переходе не передается значение поиска без использования сессии для сохранения данных поиска

    content = {
        'search_result': search_result,
        'userinput': userinput,
    }

    return render(request, 'blog/search_page.html', content)
