

# Create your views here.
from django.shortcuts import render
from .models import Blog

def blog(requset):
    post=Blog.objects.all()
    return render(requset,'blog/blog.html',{'post':post})