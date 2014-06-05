from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=40)
    product_info = models.CharField(max_length=200)
    product_price = models.DecimalField(decimal_places=2, max_digits=10)
    available = models.CharField(max_length=20)