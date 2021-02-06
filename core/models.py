from django.db import models
from django.conf import settings


# Create your models here.

# Items you see in shop.
class Item(models.Model):
    title = models.CharField(max_length=128)
    price = models.FloatField()

    def __str__(self):
        return self.title

# Items that make up an Order. Link between items and orders
class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    def __str__(self):
        return self.item.title

# Holds all the items that are part of an order
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username