from django.urls import path
from .views import *

#namespace the application
app_name = 'formapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    #path('new_post/', views.PostView.as_view(), name='post_view'),
    path('thanks/', ThanksView.as_view(), name='thanks'),
    path('blogpost/add/', BlogPostCreate.as_view(), name='blogpost-add'),
    path('blogpost/<uuid:pk>/', BlogPostInfo.as_view(), name='post-info'),
    path('blogpost/<uuid:pk>/comment/', add_comment, name='comment-add'),
    path('blogpost/all/', AllBlogPosts.as_view(), name='all-blogposts'),
    path('blogpost/search/', SearchResults.as_view(), name='search-results'),
    
]
