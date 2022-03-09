from django.db import models
from django.core.validators import MinValueValidator

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name



# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, related_name='products',on_delete=models.CASCADE)
    image = models.URLField()
    price = models.DecimalField(max_digits=6, decimal_places=2,validators=[MinValueValidator(0)])
    stock = models.IntegerField(default = 0, validators=[MinValueValidator(0)])
    status = models.CharField(max_length=50, default ='active',choices = [('active','active'),('inactive','inactive')])
    units = models.CharField(max_length=100)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_time']

    def __str__(self):
        return self.name
    



