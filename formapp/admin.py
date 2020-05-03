from django.contrib import admin

# Register your models here.

from .models import *

class CommentInline( admin.TabularInline):
    model = Comment
    extra = 5

class BlogAdmin( admin.ModelAdmin):
    fields = '__all__'
    inlines = [CommentInline]
    list_display = ('post_content', 'pub_date')
    search_fields = ['post_content']

