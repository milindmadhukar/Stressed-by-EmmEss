from django.shortcuts import render
from menu.models import Product

def menu(request): 
    carosuel_slides = []
    categories = []
    for category in Product.categories:
        carosuel_slides.append(Product.objects.filter(product_category=category[0]))
        categories.append(category[0])
    print(carosuel_slides)
    context = {"categories":categories,"carosuel_slides":carosuel_slides,}
    return render(request ,'menu/menu.html', context=context)