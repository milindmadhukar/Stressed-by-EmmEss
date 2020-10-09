from django.db import models
from menu.models import Product

class CarouselSlide(models.Model):
    carousel_id = models.AutoField(primary_key=True)
    carousel_name = models.CharField(max_length = 200, default = "")
    carousel_category = models.CharField(max_length = 110, choices=Product.categories)
    image_link = models.CharField(max_length = 500, default = "")

    def __str__(self):
        return self.carousel_name
