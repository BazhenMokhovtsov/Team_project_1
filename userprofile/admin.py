from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class AdminUserProfile(admin.ModelAdmin):
    list_display = ['user']
    search_fields = ['user']