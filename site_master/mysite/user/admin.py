from django.contrib import admin

# Register your models here.
from .models import *




class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'bio', 'profile_pic', 'vk', 'instagram')
    list_display_links = ('id', 'user')
    search_fields = ('user',)
    list_filter = ('user',)

admin.site.register(UserProfile, UserProfileAdmin)