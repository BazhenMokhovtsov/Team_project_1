from django.contrib import admin
from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title']


@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['update_date']
    search_fields = ['title']


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = [ 'author', 'post']
    search_fields = ['author']
    list_filter = ['created_date']


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = [ 'first_name', 'last_name']

