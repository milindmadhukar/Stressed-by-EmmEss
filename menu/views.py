from django.shortcuts import render
from menu.models import Product

def menu(request): 
    categories = []
    for category in Product.categories:
        categories.append(category[0])
    context = {"categories":categories}
    return render(request ,'menu/menu.html', context=context)