# blog/admin.py

from django.contrib import admin
from .models import Post, Category, UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'website')
    search_fields = ('user__username', 'user__email')

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'category', 'author')
    list_filter = ('pub_date', 'category', 'author')
    search_fields = ('title', 'content')


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(UserProfile, UserProfileAdmin)