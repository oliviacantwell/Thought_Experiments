from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def theories(request):
    return render(request,'theories.html')

def prisoner(request):
    return render(request,'prisoner.html')