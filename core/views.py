from django.shortcuts import render

# Local
from .models import Item, Order, OrderItem

# Create your views here.

def item_list(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "home-page.html", context)

def product_list(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "product-page.html", context)

def checkout_view(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "checkout-page.html", context)
