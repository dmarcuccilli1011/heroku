from django.contrib import admin

# Register your models here.

from .models import *

class CommentInline( admin.TabularInline):
    model = Comment
    extra = 1

class BlogAdmin( admin.ModelAdmin):
    inlines = [CommentInline]
    list_display = ('username', 'post_content', 'pub_date')
    search_fields = ['post_content', 'username']

admin.site.register(BlogPost, BlogAdmin)