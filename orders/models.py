from django.db import models
from django.contrib.auth.models import User 
from accounts.models import Address 
from products.models import Product
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    shipping_address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    order_time = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(max_length=50, default='pending', choices = [('pending','pending'),('delivered','delivered')])

    def __str__(self):
        return "{} - {} - {} - {}".format(self.user, self.order_status, self.shipping_address,  self. order_time)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete= models.CASCADE, null=True)
    # user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000)])
    price = models.DecimalField(max_digits=6, decimal_places=2,validators=[MinValueValidator(0)])

    def __str__(self):
        return "{} - {} - {} - {}".format(self.id, self.product, self.quantity,  self. price)

