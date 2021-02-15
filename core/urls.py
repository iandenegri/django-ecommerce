from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .views import checkout, HomeView, ItemDetailView, OrderSummaryView, add_to_cart, delete_from_cart, add_to_order_summary, delete_one_from_order_summary, delete_all_from_order_summary

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout/', checkout, name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order_summary'),
    path('item/<slug>', ItemDetailView.as_view(), name='item_detail'),
    path('add-to-cart/<slug>', add_to_cart, name='add_to_cart'),
    path('delete-from-cart/<slug>', delete_from_cart, name='delete_from_cart'),
    path('add-to-order-summary/<slug>', add_to_order_summary, name='add_to_order_summary'),
    path('delete-one-from-order-summary/<slug>', delete_one_from_order_summary, name='delete_one_from_order_summary'),
    path('delete-all-from-order-summary/<slug>', delete_all_from_order_summary, name='delete_all_from_order_summary'),
]