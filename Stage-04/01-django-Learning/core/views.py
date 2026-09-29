from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# 1 . for understanding
# from django.http import HttpResponse

# def home(request):              #This is our Function-Based View.
#     return HttpResponse("Hello from Django!")

post = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]

def home(request):
    context = {"posts":post}
    return render(request , 'core/home.html',context)        #give context to template

def about(request):
    return render(request,'core/about.html' , {"title":"About Page"})