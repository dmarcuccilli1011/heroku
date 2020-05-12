from django.db import models
from django.utils import timezone
import datetime, uuid # uuid is important
from django.forms import ModelForm, TimeInput, DateTimeInput
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from django import forms
# Create your models here.

class BlogPost(models.Model):
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False
    )
    ADMIN = 'admin' # note admin choice should not be available to users
    SPORTS = 'sports' # so we have a way for users to quickly find posts i deem important
    ANIMALS = 'animals'
    NEWS = 'news'
    COMPUTER_SCIENCE = 'computer science'
    TECHNOLOGY = 'technology'
    FINANCE = 'finance'
    OTHER = 'other'
    SCIENCE = 'science'
    HEALTH = 'health'
    WEATHER = 'weather'
    SPORTS = 'sports'
    TV = 'tv'
    MEMES = 'memes'
    TRAVEL = 'travel'
    MUSIC = 'music'
    ART = 'artistic'
    MINDBLOWING = 'mindblowing'
    CUTE = 'cute'
    PANDEMICS = 'coronavirus'
    BOOKS = 'books'
    selection_choices = [
        (SPORTS, 'sports'),
        (ANIMALS, 'animals'),
        (NEWS, 'news'),
        (COMPUTER_SCIENCE, 'computer science'),
        (TECHNOLOGY, 'technology'),
        (FINANCE, 'finance'),
        (OTHER, 'other'),
        (SCIENCE, 'science'),
        (HEALTH, 'health'),
        (WEATHER, 'weather'),
        (SPORTS, 'sports'),
        (TV, 'tv'),
        (MEMES, 'memes'),
        (TRAVEL, 'travel'),
        (MUSIC, 'music'),
        (ART, 'artisic'),
        (MINDBLOWING, 'mindblowing'),
        (CUTE, 'cute'),
        (PANDEMICS, 'coronavirus'),
        (BOOKS, 'books'),
    ]
    username = models.CharField(max_length=100, name='username', default='choose any username')
    post_content = models.TextField(max_length=500,default='type your post here')
    pub_date = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=20, choices=selection_choices, default=OTHER)

    class Meta:
        verbose_name_plural = 'Posts'
    
    def __str__(self):
        return self.username + ':  ' + self.post_content + '~~~~~~' + str(self.pub_date)

    def get_absolute_url(self):
        return reverse('post-info', args=[str(self.id)])
    


class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    #username = models.CharField(max_length=100, verbose_name='username', default='choose any username')
    username = models.TextField(max_length=125, default="username")
    comment_content = models.TextField(max_length=250, default='type your comment here')
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Comments'
    
    def __str__(self):
        return self.username + ': --->' + self.comment_content

#model forms go here

class BlogPostForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = ('username', 'post_content', 'category')
        widgets = {
            'username': forms.HiddenInput(),
        }


