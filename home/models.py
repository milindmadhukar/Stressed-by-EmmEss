from django.db import models
from menu.models import Product

class CarouselSlide(models.Model):
    carousel_id = models.AutoField(primary_key=True)
    carousel_name = models.CharField(max_length = 200, default = "")
    carousel_category = models.CharField(max_length = 110, choices=Product.categories)
    carousel_image = models.ImageField(upload_to="home/images",default = "")

    def __str__(self):
        return self.carousel_name
