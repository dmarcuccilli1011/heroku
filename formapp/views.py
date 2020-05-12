from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views import generic, View
from django.views.decorators.http import require_http_methods
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from django.contrib.auth import get_user_model
from django.db.models import Q

#imports from this application below
from formapp.forms import CommentForm
from .models import *

# views start here
class IndexView( generic.ListView ):
    template_name = 'formapp/index.html'
    context_object_name = 'hello_world'

    def get_queryset(self):
        posts = BlogPost.objects.order_by('-pub_date')[:5]
        return {
            'blog_posts': posts,
            'value1': 'oh', 
            'value2': 'fuck', 
            'value3': 42,
             }

class BlogPostCreate(CreateView):
    template_name = 'formapp/forms.html'
    model = BlogPost
    form_class = BlogPostForm # BlogPostForm is found in /formapp/models
    success_url = '/formapp/thanks/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user = self.request.user
        empty_form = BlogPostForm(initial={'username': current_user})
        
        context['form'] = empty_form
        return context

class ThanksView( generic.TemplateView):
    template_name = 'formapp/thanks.html'

# class to display all existing posts, ideally 25 at a time or so
class AllBlogPosts( generic.ListView ):
    model = BlogPost
    template_name = 'formapp/all_posts.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        payload = BlogPost.objects.all()
        return payload

# below we use CommentForm, found in formapp/forms. this is a bit confusing
class BlogPostInfo(generic.DetailView):
    model = BlogPost
    template_name = 'formapp/post_info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        some_data = str(self.request) # manually strip out the primary key because i suck 
        some_list = some_data.split('/')
        primary_key = some_list[-2]
        the_key = BlogPost.objects.get(pk=primary_key)
        current_user = self.request.user
        the_form = CommentForm(initial={'blog_post': the_key, 'username': current_user})
        
        context['form'] = the_form
        return context

class SearchResults( generic.ListView ):
    model = BlogPost
    context_object_name = 'post_list'
    template_name = 'formapp/search_results.html'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        return BlogPost.objects.filter(
            Q(username__icontains=query) | Q(post_content__icontains=query) | Q(category__icontains=query)
        )

class CategorySearchView( generic.ListView ):
    model = BlogPost
    context_object_name = 'post_list'
    template_name = 'formapp/search_results.html'

    def get_queryset(self): 
        query = self.request.GET.get('q')
        return BlogPost.objects.filter(
            Q(category__icontains=query)
        )


def add_comment(request, pk):
    blogpost_id = pk
    the_form = CommentForm(request.POST)

    new_comment = the_form.save()
    #blogpost = get_object_or_404(BlogPost, pk=blogpost_id)

    return HttpResponseRedirect(reverse('formapp:post-info', args=(blogpost_id,)))





#@require_http_methods(["GET", "POST"])
#class PostView( generic.FormView):
#    template_name = 'formapp/post_form.html'

