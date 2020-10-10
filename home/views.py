from django.shortcuts import render, HttpResponse, redirect

# HTML Pages

def home(request):
    return render(request, 'home/home.html')

def aboutUs(request):
    return render(request, 'home/aboutus.html')

