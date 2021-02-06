from django.db import models
from django.conf import settings
from django.shortcuts import reverse


# Items you see in shop.
class Item(models.Model):
    CATEGORY_CHOICES = [
        ('shirt', 'Shirt'),
        ('sport', 'Sports Wear'),
        ('outer', 'Outerwear')
    ]

    LABEL_CHOICES = [
        ('pri', 'primary'),
        ('sec', 'secondary'),
        ('dan', 'danger')
    ]
    title = models.CharField(max_length=128)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=10)
    label = models.CharField(choices=LABEL_CHOICES, max_length=10)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('core:item_detail', kwargs={
            'slug': self.slug
        })

    def get_add_to_cart_url(self):
        return reverse('core:add_to_cart', kwargs={
            'slug': self.slug
        })

    def get_delete_from_cart_url(self):
        return reverse('core:delete_from_cart', kwargs={
            'slug': self.slug
        })

# Items that make up an Order. Link between items and orders
class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title} for {self.user}'s order"

# Holds all the items that are part of an order
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField(blank=True, null=True)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username