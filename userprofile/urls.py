from django.urls import path
from django.http import HttpResponse
from . import views

app_name = 'userprofile'

urlpatterns = [

      path('', views.user_profile, name='user_profile'),
      path('login/', views.user_login, name='user_login'),
      path('register/', views.register, name='register'),
]