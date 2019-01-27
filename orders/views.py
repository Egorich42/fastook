from django.shortcuts import render
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from django.conf import settings
from django.contrib.sessions.backends.db import SessionStore


def OrderCreate(request):
    user = request.user
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()

            for item in cart:
                OrderItem.objects.create(order = order, 
                                         product = item['product'],
                                         price =item['price'],
                                         quantity = item['quantity'],
                                         sess_id = request.session.session_key)
            cart.clear()
            return render(request, 'orders/thanks.html', {'order': order})

    form = OrderCreateForm()
    return render(request, 'orders/order.html', {'cart': cart, 'form': form})
    pass

   