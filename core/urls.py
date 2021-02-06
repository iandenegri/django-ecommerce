from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .views import checkout, HomeView, ItemDetailView, add_to_cart, delete_from_cart

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('item/<slug>', ItemDetailView.as_view(), name='item_detail'),
    path('checkout/', checkout, name='checkout'),
    path('add-to-cart/<slug>', add_to_cart, name='add_to_cart'),
    path('delete-from-cart/<slug>', delete_from_cart, name='delete_from_cart')
]