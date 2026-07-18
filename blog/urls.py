from django.urls import path
from blog.views import *

app_name='blog'
urlpatterns=[
    path('',blog_view,name='index'),
    path('single-block',single_block,name='single'),
    path('post-<int:pid>',test_view,name='test')
    
]

