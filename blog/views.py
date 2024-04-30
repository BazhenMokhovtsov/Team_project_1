from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Category, Posts

def index(reques):
    return HttpResponse ("hallo")


def show_all_categories(request):
    categories = Category.objects.all()

    content = {

        'categories': categories,
    }

    return render(request, 'blog/1st_page.html', content)

# def single_category(request, category_id):
#     category = Category.objects.get(pk=category_id)

#     content = {
#         "category": category
#     }

#     return render(request, "blog/single_category.html", content)








def show_posts_to_category(request):
    posts = Posts.objects.filter(category__title='Новости')

    content = {

        "posts": posts,

    }

    return render(request, 'blog/category_posts.html', content)


def show_single_post(request, post_id):
    post = Posts.objects.get(pk=post_id)

    content = {
        "post": post
    }

    return render(request, "blog/single_post.html", content)