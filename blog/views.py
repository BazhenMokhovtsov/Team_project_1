from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Category, Posts, Comments
from .forms import CommentForm

def index(reques):
    return HttpResponse ("hallo")


def show_all_categories(request):
    categories = Category.objects.all()

    content = {

        'categories': categories,
    }

    return render(request, 'blog/1st_page.html', content)


def show_posts_to_category(request, category_id):
    
    posts = Posts.objects.filter(category__id=category_id)

    content = {

        "posts": posts,

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



    

