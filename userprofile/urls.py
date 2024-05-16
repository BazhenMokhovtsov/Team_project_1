from django.urls import path
from django.http import HttpResponse
from . import views

app_name = 'userprofile'

urlpatterns = [

      path('', views.user_profile, name='user_profile'),
      path('<int:post_id>/', views.user_profile, name='edit_post'),
      path('login/', views.user_login, name='user_login'),
      path('register/', views.register, name='register'),
      path('del_post/<int:post_id>/', views.del_post, name='del_post'),
      path('<int:post_id>/', views.user_profile, name='user_profile'),
]