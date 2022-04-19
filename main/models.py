from pickle import TRUE
from tkinter import CASCADE
from turtle import title
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BlogCategory(models.Model):
        title=models.CharField(max_length=100, default="uncategories")
        slug=models.SlugField(unique=True)
        image=models.ImageField(upload_to='category/', null=True, blank=True)
        active=models.BooleanField(default=True)
        created_at=models.DateTimeField(auto_now_add=True)
        updated_at=models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return self.title

class BlogPost(models.Model):
        user=models.ForeignKey(User, on_delete=models.CASCADE)
        category=models.ForeignKey(BlogCategory,on_delete=models.CASCADE,default="4")
        title= models.CharField(max_length=100)
        description=models.TextField()
        image=models.ImageField(upload_to='blog/', null=True, blank=True)
        active=models.BooleanField(default=True)
        created_at=models.DateTimeField(auto_now_add=True)
        updated_at=models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return self.title
