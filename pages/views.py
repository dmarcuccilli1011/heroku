from django.shortcuts import render
from django.views.generic import TemplateView, ListView
# Create your views here.

class HomePageView( TemplateView ):
    template_name = 'home.html'

class AboutPageView( TemplateView ):
    template_name = 'about.html'

class UserHomeView( TemplateView ):
    template_name = 'user_home.html'

class GraphicalHomeView( TemplateView ):
    template_name = 'graphics_home.html'

class SVGDemoView( ListView ):
    template_name = 'svg_demo.html'
    context_object_name = 'view_data'
    

    def get_queryset(self):
        return ''

class MagicCubeView( TemplateView ):
    template_name = '3D.html'