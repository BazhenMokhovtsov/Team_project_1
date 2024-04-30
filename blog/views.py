from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Category

def index(reques):
    return HttpResponse ("hallo")


def show_all_categories(request):

    categories = Category.objects.all()

    content = {

        'categories': categories,
    }

    return render(request, 'blog/1st_page.html', content)