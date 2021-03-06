from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, View
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Local
from .models import Item, Order, OrderItem


# Create your views here.
# CBV's
class HomeView(ListView):
    model = Item
    paginate_by = 10
    template_name = 'home.html'


class ItemDetailView(DetailView):
    model = Item
    template_name = 'item.html'


def checkout(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "checkout.html", context)


class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object': order 
            }
            return render(self.request, 'order_summary.html', context=context)
        except Order.DoesNotExist:
            messages.error(self.request, "You don't have an active order.")
            return redirect("/")


# FBV's
@login_required
def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order, created = Order.objects.get_or_create(user=request.user, ordered=False) # The user should only have one on going order that is False. If they don't have one at all, we should create one, right?
    if created:
        order_item = OrderItem.objects.create(item=item, user=request.user)
        order.items.add(order_item)
    else:
        # Check if the item is in the order
        if order.items.filter(item=item).exists():
            order_item = order.items.get(item=item)
        else:
            order_item = OrderItem.objects.create(item=item, user=request.user)
            messages.success(request, "This item was added to your cart.")
        if order.items.filter(item__slug=item.slug).exists():
            # If it's already in the order then they're trying to add more to the order.
            order_item.quantity += 1
            order_item.save()
            messages.success(request, f"This item was added to your cart. Item quantity increased to {order_item.quantity}.")
        else:
            order.items.add(order_item)
    return redirect('core:item_detail', slug = slug)


@login_required
def delete_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    try:
        order = Order.objects.get(user = request.user, ordered = False)
    except Order.DoesNotExist:
        messages.warning(request, "You currently don't have an active order!")
        return redirect('core:item_detail', slug = slug)
    # Check if the item is in the order
    if order.items.filter(item=item).exists():
        order_item = order.items.get(item=item)
    else:
        # Return an error message or something...
        messages.warning(request, "This item does not exist in your cart!")
        return redirect('core:item_detail', slug = slug)
    # Check if we have 1. If so, just delete that order's order item.
    if order_item.quantity == 1:
        order_item.delete()
        messages.success(request, "This item was removed from your cart.")
    # Otherwise, we reduce the quantity by 1.
    else:
        order_item.quantity -= 1
        order_item.save()
        messages.success(request, f"One copy of this item was removed from your cart. Item quantity is now {order_item.quantity}.")
    return redirect('core:item_detail', slug = slug)


@login_required
def add_to_order_summary(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order, created = Order.objects.get_or_create(user=request.user, ordered=False) # The user should only have one on going order that is False. If they don't have one at all, we should create one, right?
    if created:
        order_item = OrderItem.objects.create(item=item, user=request.user)
        order.items.add(order_item)
    else:
        # Check if the item is in the order
        if order.items.filter(item=item).exists():
            order_item = order.items.get(item=item)
        else:
            order_item = OrderItem.objects.create(item=item, user=request.user)
            messages.success(request, "This item was added to your cart.")
        if order.items.filter(item__slug=item.slug).exists():
            # If it's already in the order then they're trying to add more to the order.
            order_item.quantity += 1
            order_item.save()
            messages.success(request, f"This item was added to your cart. Item quantity increased to {order_item.quantity}.")
        else:
            order.items.add(order_item)
    return redirect('core:order_summary')


@login_required
def delete_one_from_order_summary(request, slug):
    item = get_object_or_404(Item, slug=slug)
    try:
        order = Order.objects.get(user = request.user, ordered = False)
    except Order.DoesNotExist:
        messages.warning(request, "You currently don't have an active order!")
        return redirect('core:order_summary')
    # Check if the item is in the order
    if order.items.filter(item=item).exists():
        order_item = order.items.get(item=item)
    else:
        # Return an error message or something...
        messages.warning(request, "This item does not exist in your cart!")
        return redirect('core:order_summary')
    # Check if we have 1. If so, just delete that order's order item.
    if order_item.quantity == 1:
        order_item.delete()
        messages.success(request, "This item was removed from your cart.")
    # Otherwise, we reduce the quantity by 1.
    else:
        order_item.quantity -= 1
        order_item.save()
        messages.success(request, f"One copy of this item was removed from your cart. Item quantity is now {order_item.quantity}.")
    return redirect('core:order_summary')


@login_required
def delete_all_from_order_summary(request, slug):
    item = get_object_or_404(Item, slug=slug)
    try:
        order = Order.objects.get(user = request.user, ordered = False)
    except Order.DoesNotExist:
        messages.warning(request, "You currently don't have an active order!")
        return redirect('core:order_summary')
    # Check if the item is in the order
    if order.items.filter(item=item).exists():
        order_item = order.items.get(item=item)
    else:
        # Return an error message or something...
        messages.warning(request, "This item does not exist in your cart!")
        return redirect('core:order_summary')
    order_item.delete()
    messages.success(request, "This item was removed from your cart.")
    return redirect('core:order_summary')
