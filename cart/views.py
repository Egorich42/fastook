from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from taverns.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from django.contrib.sessions.backends.db import SessionStore
from orders.models import OrderItem
from django.views.generic import ListView

@require_POST
def CartAdd(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'],
                                  update_quantity=cd['update'])
    return redirect('cart:CartDetail')



def CartRemove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:CartDetail')

def CartDetail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
                                                                    'quantity': item['quantity'],
                                                                    'update': True
                                                                    })

    return render(request, 'cart/cart_detail.html', {'cart': cart})


class OrdersDeatil(ListView):
    model = OrderItem
    context_object_name = 'my_orders'

    def get_queryset(self):
        result = OrderItem.objects.filter(sess_id = self.request.session.session_key) 
        if len(result) < 1:
            result = 'no orders'
        return result
        pass

    def get_template_names(self):
        return ['cart/current_orders.html']
        pass