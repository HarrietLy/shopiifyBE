from django.db import models
from django.contrib.auth.models import User 
from products.models import Product
from django.core.validators import MinValueValidator

# Create your models here.
class CartItem(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, validators=[MinValueValidator(1)])
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - {} - {} - {}".format(self.user,self.product, self.quantity, self.created_time)