from django.urls import path

from .views import *

urlpatterns = [
    path('category/', CategoryList.as_view(), name='category-list'),
    path('category/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
    path('category/create/', CategoryCreate.as_view(), name='category-create'),
    path('posts/', PostAPIList.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostAPIDetail.as_view(), name='post-detail'),
    path('posts/create/', PostAPICreate.as_view(), name='post-create'),
    path('posts/update/<int:pk>/', PostAPIUpdate.as_view(), name='post-update'),
    path('comments/', CommentsAPIList.as_view(), name='comments-list'),
    path('comments/delete/<int:pk>/', CommentsAPIDelete.as_view(), name='comments-delete'),
]
