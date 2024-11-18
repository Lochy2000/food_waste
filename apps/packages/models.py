from django.db import models

# Create your models here.

class FoodPackage(models.Model):
    restaurant = models.ForeignKey('restaurants.Restaurant', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    original_price = models.DecimalField(max_digits=6, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField()
    available_from = models.DateTimeField()
    available_until = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)