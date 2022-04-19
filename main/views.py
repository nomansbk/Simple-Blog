from multiprocessing import context
from django.shortcuts import render

from .models import BlogPost

# Create your views here.
def HomeView(request):
    posts=BlogPost.objects.all().order_by("-id")
    context={
        'posts':posts
    }
   
    return render (request,'home.html',context)

def SingleBlogView(request,id):
    single_post=BlogPost.objects.get(id=id)
    context={
            'single_post':single_post
    }
    return render (request,'single-post.html',context)
