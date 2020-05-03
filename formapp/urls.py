from django.urls import path
from .views import *

#namespace the application
app_name = 'formapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    #path('new_post/', views.PostView.as_view(), name='post_view'),
    path('thanks/', ThanksView.as_view(), name='thanks'),
    path('blogpost/add/', BlogPostCreate.as_view(), name='blogpost-add'),
    path('blogpost/<int:pk>/', BlogPostInfo.as_view(), name='post-info'),
    path('blogpost/<int:blogpost_id>/comment/', add_comment, name='comment-add'),
]
