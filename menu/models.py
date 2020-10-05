from django.db import models

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(default="", max_length=300)

    categories = (
        ("Brigadeiro","Brigadeiro"),
        ("Brownie","Brownie"),
        ("Cake","Cake"),
        ("Cheesecake","Cheesecake"),
        ("Chef's Special","Chef's Special"),
        ("Cupcakes","Cupcakes"),
        ("Fudges","Fudges"),
        ("Tea Time","Tea Time"),
    )

    product_category = models.CharField(max_length = 110, choices=categories)

    product_preview_image = models.ImageField(upload_to="menu/images", default="")

    product_price = models.PositiveIntegerField(default = 0)

    def __str__(self):
        return self.product_name + "- Rs " + self.prduct_price

    
