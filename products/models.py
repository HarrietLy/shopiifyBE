from django.db import models


class Category(models.model):
    name = models.CharField(max_length=100)

# Create your models here.
class Product(models.model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='products',on_delete=models.CASCADE)
    image = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    stock = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    units = models.CharField(max_length=100)
    



