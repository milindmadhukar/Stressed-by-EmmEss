from django.shortcuts import render, HttpResponse, redirect

# HTML Pages

def home(request):
    return render(request, 'home/home.html')

