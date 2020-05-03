from django.db import models
from django.utils import timezone
import datetime
from django.forms import ModelForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
# Create your models here.

class BlogPost(models.Model):
    username = models.CharField(max_length=100, name='username', default='choose any username')
    post_content = models.TextField(max_length=500,default='post about anything you want, please try to keep it polite')
    pub_date = models.DateTimeField('Date Published', default=timezone.now)

    class Meta:
        verbose_name_plural = 'Posts'
    
    def __str__(self):
        return self.username + ':  ' + self.post_content + '~~~~~~' + str(self.pub_date)


class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    #username = models.CharField(max_length=100, verbose_name='username', default='choose any username')
    username = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    comment_content = models.TextField(max_length=250, default='say anything you want, please try to keep it polite')
    timestamp = models.TimeField('timestamp', default=timezone.now)

    class Meta:
        verbose_name_plural = 'Comments'
    
    def __str__(self):
        return self.username + ': --->' + self.comment_content

#model forms go here

class BlogPostForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = '__all__'

