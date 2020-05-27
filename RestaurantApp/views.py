from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    return render(request , 'index.html')

def contactUs(request):
    return render(request , 'contactUs.html')

def aboutUs(request):
    return render(request , 'aboutUs.html')