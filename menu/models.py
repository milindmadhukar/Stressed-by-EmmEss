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
        ("Cupcake","Cupcake"),
        ("Fudge","Fudge"),
        ("Tea Time","Tea Time"),
    )

    product_category = models.CharField(max_length = 110, choices=categories)

    product_image_link = models.CharField(max_length = 500)

    product_price = models.PositiveIntegerField(default = 0)

    def __str__(self):
        return f"{self.product_name} - Rs {self.product_price}"

    def get(self, value):
        vals = {'product_id':self.product_id,'product_name':self.product_name, 'product_image_link':self.product_image_link, 'product_price':self.product_price}

        return vals.get(value)

    
