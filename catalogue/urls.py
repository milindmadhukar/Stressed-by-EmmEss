from django.contrib import admin
from django.urls import path
from catalogue import views

urlpatterns = [
    path('', views.catalogue, name='catalogue'),
]