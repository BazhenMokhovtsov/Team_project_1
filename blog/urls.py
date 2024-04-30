from django.urls import path
from django.http import HttpResponse
from . import views

app_name = 'blog'

urlpatterns = [

    path('', views.index),
    path('categories', views.show_all_categories, name='show_all_categories'),
    path('posts', views.show_posts_to_category, name = 'show_posts_to_category'),
    path('single_post/<int:post_id>',views.show_single_post, name='show_single_post' )



]
