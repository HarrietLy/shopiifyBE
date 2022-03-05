from django.db import models
from django.contrib.auth.models import User 


# Create your models here.
class Address(models.Model):
    shipping_address = models.CharField(max_length=200)
    user = models.ForeignKey(User,related_name="addresses",on_delete=models.CASCADE)

    def __str__(self):
        return self.shipping_address
