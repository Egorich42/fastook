from django.shortcuts import render
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from django.conf import settings


def OrderCreate(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            return render(request, 'orders/thanks.html', {'order': order})

    orders_for_place_wait = OrderItem.objects.all()
    for x in orders_for_place_wait:
        print(x.order.session_key)

    form = OrderCreateForm()
    return render(request, 'orders/order.html', {'cart': cart, 
                                                        'form': form})


#bpgkaj2t5gtu99h2vlfqffcxkgrkc8bn
#bpgkaj2t5gtu99h2vlfqffcxkgrkc8bn    