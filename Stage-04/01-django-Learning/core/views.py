from django.shortcuts import render

# Create your views here.

# 1 . for understanding
# from django.http import HttpResponse

# def home(request):              #This is our Function-Based View.
#     return HttpResponse("Hello from Django!")

def home(request):
    name = 'kesha'
    return render(request , 'home.html',{'name':name})        #give context to template