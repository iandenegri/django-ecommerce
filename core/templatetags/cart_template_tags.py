from django import template

from core.models import Order, OrderItem

register = template.Library()

@register.filter
def cart_item_count(user):
    if user.is_authenticated:
        try:
            active_order = Order.objects.get(user=user, ordered=False)
        except Order.DoesNotExist:
            active_order = None
        if active_order:
            return active_order.cart_item_count()
        else:
            return 0
