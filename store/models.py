from django.db import models

# Create your models here.

class Product (models.Model):
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=7 , decimal_places=2)
    added_at = models.DateField(auto_now_add= True)
    updated_at = models.DateField(auto_now=True)
    in_stock = models.BooleanField(default=True)