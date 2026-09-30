from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

# 1 . for understanding
# from django.http import HttpResponse

# def home(request):              #This is our Function-Based View.
#     return HttpResponse("Hello from Django!")

def home(request):
    context = {"posts": Post.objects.all()}
    return render(request , 'core/home.html',context)        #give context to template

def about(request):
    return render(request,'core/about.html' , {"title":"About Page"})