from django.contrib import admin

# Register your models here.

from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("title",)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'bio', 'profile_pic', 'vk', 'instagram')
    list_display_links = ('id', 'user')
    search_fields = ('user',)
    list_filter = ('user',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(UserProfile, UserProfileAdmin)