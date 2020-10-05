from django.shortcuts import render, HttpResponse, redirect
from home.models import CarouselSlide
from menu.models import Product

# HTML Pages

def home(request):
    carosuel_slides = []
    categories = []
    for category in Product.categories:
        carosuel_slides.append(CarouselSlide.objects.filter(carousel_category=category[0]))
        categories.append(category[0])
    context = {"carosuel_slides":carosuel_slides, "categories":categories}
    return render(request ,'home/home.html', context=context)
