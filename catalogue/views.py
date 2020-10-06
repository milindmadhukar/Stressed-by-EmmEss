from django.shortcuts import render
from catalogue.models import CarouselSlide
from menu.models import Product

def catalogue(request):
    carosuel_slides = []
    categories = []
    for category in Product.categories:
        carosuel_slides.append(CarouselSlide.objects.filter(carousel_category=category[0]))
        categories.append(category[0])
    context = {"carosuel_slides":carosuel_slides, "categories":categories}
    return render(request ,'catalogue/catalogue.html', context=context)
