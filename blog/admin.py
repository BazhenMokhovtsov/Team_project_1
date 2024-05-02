from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']
    list_filter = ['update_date']
    search_fields = ['category']
    prepopulated_fields = {'slug': ('title',)}


    
@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['author', 'post']
    list_filter = ['created_date']
    search_fields = ['post']

