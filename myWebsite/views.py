from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home(request):
    return render(request, 'home.html')

def About(request):
    return render(request, 'about.html')

def Contact(request):
    return HttpResponse('This is my Contact Page. Welcome to my world!')