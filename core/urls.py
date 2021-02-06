from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .views import item_list, product_list, checkout_view

app_name = 'core'

urlpatterns = [
    path('', item_list, name='item-list'),
    path('products/', product_list, name='product-list'),
    path('checkout/', checkout_view, name='checkout')
]