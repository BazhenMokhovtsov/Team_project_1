from django.urls import path

from .views import *

urlpatterns = [
    path('category/', CategoryList.as_view(), name='category-list'),
    path('category/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
    path('category/create/', CategoryCreate.as_view(), name='category-create'),
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/create/', PostList.as_view(), name='post-detail'),
]
