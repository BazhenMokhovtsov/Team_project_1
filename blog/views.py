from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Category, Posts, Comments
from .forms import CommentForm, SortPostForm
from django.core.paginator import Paginator
from django.db.models import Q


def paginator_page(request, queryset, pages):
    paginator = Paginator(queryset,pages)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj
    

def show_all_categories(request):
    categories = Category.objects.all()  # 
    #posts = Posts.objects.all() много лишних переменных. можно сделать все действия с одной переменной.

    if request.method =='POST':
        sort_form = SortPostForm(request.POST)
        if sort_form.is_valid():
            sort_by = sort_form.cleaned_data['sort_by']
            if sort_by == 'update_date':
                sorted_posts = Posts.objects.order_by('update_date')
            elif sort_by == 'category':
                sorted_posts = Posts.objects.order_by('category_id')
            else:
                sorted_posts = Posts.objects.filter(published=True)
    
            posts = sorted_posts # тут крылась ошибка. На этой строке должна быть сортировка.
            page_obj = paginator_page(request,posts,2)
        
            content = {
                'sort_form': sort_form,
                'sorted_posts': sorted_posts,
                'page_obj': page_obj,
            }

            return render(request, 'blog/1st_page.html', content)
    else:
        sort_form = SortPostForm()

    posts = Posts.objects.filter(published=True) 
    page_obj = paginator_page(request,posts,2)

    content = {
            'sort_form': sort_form,
            'categories': categories,
            'page_obj': page_obj,
        }
    
    return render(request, 'blog/1st_page.html', content)


def show_posts_to_category(request, category_id): 
    posts = Posts.objects.filter(category__id=category_id, published=True)

    page_obj = paginator_page(request,posts,2)

    content = {

        "posts": posts,
        "page_obj": page_obj,
    }

    return render(request, 'blog/category_posts.html', content)


def show_single_post(request, post_id):
    single_post = Posts.objects.get(pk=post_id)
    comments = Comments.objects.filter(post__id=post_id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.post = single_post
            post.author = request.user
            post.save()
        return redirect('blog:show_single_post')
    else:
        form = CommentForm

    content = {
        "form": form,
        "single_post": single_post,
        "comments": comments,
    }

    return render(request, "blog/single_post.html", content)


def del_comment(request,comment_id):
    comment = Comments.objects.get(pk = comment_id)
    comment.delete()

    return redirect("blog:show_single_post", post_id=comment.post.pk)

#для поиска используется бибилиотека Q sql3
def search(request):
    userinput = request.POST.get('search')
    query = Q(title__icontains=userinput) | Q(text__icontains=userinput)
    search_result = Posts.objects.filter(query, published=True)

    # search_result = paginator_page(request,search_result,1)  # Не работает...при переходе не передается значение поиска.
 
    content = {
        'search_result': search_result,
        'userinput': userinput,
    }

    return render(request, 'blog/search_page.html', content)
