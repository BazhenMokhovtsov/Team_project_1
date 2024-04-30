from django.urls import path
from django.http import HttpResponse
from . import views

app_name = 'blog'

urlpatterns = [

    path('', views.index),
    path('categories', views.show_all_categories, name='show_all_categories'),


]
