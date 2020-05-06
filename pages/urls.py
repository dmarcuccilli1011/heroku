from django.urls import path
from .views import HomePageView, AboutPageView, UserHomeView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('userhome/', UserHomeView.as_view(), name='user-homepage'),
]
