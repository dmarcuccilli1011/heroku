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
    username = models.CharField(max_length=100, name='username', default='choose any username')
    post_content = models.TextField(max_length=500,default='type your post here')
    pub_date = models.DateTimeField('Date Published', default=timezone.now)

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
    timestamp = models.TimeField('timestamp', default=timezone.now)

    class Meta:
        verbose_name_plural = 'Comments'
    
    def __str__(self):
        return self.username + ': --->' + self.comment_content

#model forms go here

class BlogPostForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = ('username', 'post_content', 'pub_date')
        widgets = {
            'username': forms.HiddenInput(),
            'pub_date': DateTimeInput(attrs={'readonly': True})
        }


