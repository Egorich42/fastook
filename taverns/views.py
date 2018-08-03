from django.shortcuts import render, get_object_or_404, render_to_response
from taverns.models import Taverna, Product
from django.views.generic.detail import DetailView
from clients.models import Client

from cart.forms import CartAddProductForm

# Create your views here.
def main(request):
	places = Taverna.objects.all()
	clients = Client.objects.all()
	for x in clients:
		print(x.name,x.get_absolute_url)
	return render(request, 'places/taverns_list.html',{'places':places})


def show_tavern(request, slug):
	place = get_object_or_404(Taverna, slug=slug)
	products = Product.objects.filter(place=place)
	return render(request, 'places/taverna.html',{'place':place, 'products': products})



def show_product(request, slug):
	product = get_object_or_404(Product, slug=slug)
	cart_product_form = CartAddProductForm()
	return render(request, 'places/eda.html',{'product': product,'cart_product_form':cart_product_form})

