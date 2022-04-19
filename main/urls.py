
from django.urls import path

from .views import *

urlpatterns = [
    path('',HomeView,name="home"),
    path('single-post-<int:id>/',SingleBlogView,name="singlepost"),
  
]