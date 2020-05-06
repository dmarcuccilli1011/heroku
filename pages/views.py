from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class HomePageView( TemplateView ):
    template_name = 'home.html'

class AboutPageView( TemplateView ):
    template_name = 'about.html'

class UserHomeView( TemplateView ):
    template_name = 'user_home.html'