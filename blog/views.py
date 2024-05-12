from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Category, Posts, Comments
from .forms import CommentForm, SortPostForm
from django.core.paginator import Paginator

def show_all_categories(request):
    categories = Category.objects.all()
    

    if request.method =='POST':
        sort_form = SortPostForm(request.POST)
        if sort_form.is_valid():
            sort_by = sort_form.cleaned_data['sort_by']
            if sort_by == 'title':
                sorted_posts = Posts.objects.order_by('title')
            elif sort_by == 'update_date':
                sorted_posts = Posts.objects.order_by('update_date')
            elif sort_by == 'category':
                sorted_posts = Posts.objects.order_by('category_id')
            else:
                sorted_posts = Posts.objects.all()
    
            posts = sorted_posts # тут кроится ошибка. На этой строке должна быть сортировка.
            paginator = Paginator(posts,2)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
        
            content = {
                'sort_form': sort_form,
                'sorted_posts': sorted_posts,
                'page_obj': page_obj,
            }

            return render(request, 'blog/1st_page.html', content)
    else:
        sort_form = SortPostForm()

    posts = Posts.objects.all() # тут кроится ошибка. На этой строке должна быть сортировка.
    paginator = Paginator(posts,2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number) 

    content = {
            'sort_form': sort_form,
            'categories': categories,
            'page_obj': page_obj,
        }
    
    return render(request, 'blog/1st_page.html', content)


def show_posts_to_category(request, category_id): 
    posts = Posts.objects.filter(category__id=category_id)
    paginator = Paginator(posts,2)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

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
        return redirect('blog:show_single_post', post_id=post_id)
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


