from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# 1 . for understanding
# from django.http import HttpResponse

# def home(request):              #This is our Function-Based View.
#     return HttpResponse("Hello from Django!")

def home(request):
    name = 'kesha'
    return render(request , 'home.html',{'name':name})        #give context to template

def about(request):
    return HttpResponse("<h1>You are in about page</h1>")