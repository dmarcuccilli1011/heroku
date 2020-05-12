from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('userhome/', UserHomeView.as_view(), name='user-homepage'),
    path('graphical/', GraphicalHomeView.as_view(), name='graphics-home'),
    path('graphical/svg-demo/', SVGDemoView.as_view(), name='svg-demo'),
    path('graphical/3D-cube/', MagicCubeView.as_view(), name='3d-cube' ),

]
