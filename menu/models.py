from django.db import models

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(default="", max_length=300)

    category = (
        ("A","Brigadeiro"),
        ("B","Brownie"),
        ("C","Cake"),
        ("D","Cheesecake"),
        ("E","Chef's Special"),
        ("F","Cupcakes"),
        ("G","Fudges"),
        ("H","Tea Time"),
    )

    product_category = models.CharField(max_length = 300, choices=category)

    # product_preview_image = models.ImageField()

    
