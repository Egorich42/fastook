#! /usr/bin/env python
# -*- coding: utf-8 -*
from django.shortcuts import render, get_object_or_404, render_to_response
from django.views.generic.edit import FormView
from django.views.generic import ListView
from django.views.generic.base import View
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from taverns.models import Taverna
from orders.models import OrderItem, Order, Product

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.db.models import Sum, Avg, FloatField

import operator

from datetime import date

from .models import Cook
from .forms import DishCreateForm

import itertools
from operator import itemgetter


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "login.html"
    success_url = "/"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)
        pass


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")
        pass






class CookPlace(ListView):
    def get(self, request, id):
        cook = get_object_or_404(Cook, id = id)
        print('suuuuka')
        if cook.status == 'cook':
            form = DishCreateForm()
            place_dishes = Product.objects.all()
            print(place_dishes,'!!!!!!!!!!!!!!!!!')
            return render(request, 'users/cook_cabinet.html', {'form':form, 'place_dishes':place_dishes})


    def post(self, request, id):

        form = DishCreateForm(request.POST)

        if form.is_valid():
            Product.objects.create(place = get_object_or_404(Taverna, id = id), 
                                    name =     request.POST['name'],
                                    slug =     request.POST['slug'],
                                     image =    request.POST['image'],
                                     price =    request.POST['price'],
                                    weight =     request.POST['weight'],
                                    description =     request.POST['description'],)
        return render(request, 'users/cook_cabinet.html')




class OwnerProfile(ListView):
    def get(self, request, id):
        user = get_object_or_404(User, id = id)

        
        taverns = Taverna.objects.filter(owner_id = user.id-1) 
        for place in taverns:
            place.orders_in_queue_count = OrderItem.objects.all().filter(product__place__id = place.id, order__item_status = Order.item_stats[0], created_at=date.today()).count()
            place.orders_paid_count = OrderItem.objects.all().filter(product__place__id = place.id, order__item_status =  Order.item_stats[2], created_at=date.today()).count()
            place.orders_paid_sum = OrderItem.objects.all().filter(product__place__id = place.id, order__item_status =  Order.item_stats[2], created_at=date.today()).aggregate(Sum('price'))['price__sum']

            if place.orders_paid_sum == None:
                place.orders_paid_sum = 0

            place.orders_paid_avg = OrderItem.objects.all().filter(product__place__id = place.id, order__item_status =  Order.item_stats[2], created_at=date.today()).aggregate(Avg('price'))['price__avg']
            if place.orders_paid_avg == None:
                place.orders_paid_avg = 0
        
            
            list_of_dicts = list(OrderItem.objects.all().filter(product__place__id = place.id).values())


            guk = []
            for x in list_of_dicts:
                guk +=[{'prod_id_in_ord': x['product_id'], 'prod_money_in_odrder': float(x['quantity'])*float(x['price']) }]
     

            guki ={}
            for x in guk:
                if x['prod_id_in_ord'] in guki:
                    guki[x['prod_id_in_ord']] += x['prod_money_in_odrder']
                else:
                    guki[x['prod_id_in_ord']] = x['prod_money_in_odrder']


            
            sorted_d = sorted(guki.items(), key=operator.itemgetter(1), reverse = True)
            dish_of_day = []

            if len(sorted_d) > 1:
                for x in range(len(sorted_d)):
                    if sorted_d[x][1] > sorted_d[x+1][1]:
                        if x+1 >= len(sorted_d)-1:
                            break
                        dish_of_day += [Product.objects.get(id = sorted_d[x][0]).name]
            if len(sorted_d) == 1:
                dish_of_day = Product.objects.get(id =sorted_d[0][0]).name

            else:
                dish_of_day = 'Нет результата' 

            place.dish_of_day = dish_of_day

        return render(request, 'users/user_profile.html', {'taverns':taverns})
        pass
        


class PostDetail(ListView):
    @method_decorator(login_required)
    def get(self, request,id,id_tavern):
        place = get_object_or_404(Taverna, id=id_tavern)
        orders_for_place_wait = OrderItem.objects.all().filter(product__place__id = place.id, order__item_status = Order.item_stats[0], created_at=date.today())
        orders_for_place_ready = OrderItem.objects.all().filter(product__place__id = place.id, order__item_status = Order.item_stats[1], created_at=date.today())
        orders_for_place_paid = OrderItem.objects.all().filter(product__place__id = place.id, order__item_status = Order.item_stats[2], created_at=date.today())

        print(orders_for_place_wait.count())
        print(orders_for_place_ready.count())
        print(orders_for_place_paid.count())

        return render(request, "users/user_place_info.html",{'orders_wait':orders_for_place_wait,
                                                              'orders_ready':  orders_for_place_ready, 
                                                              'orders_paid': orders_for_place_paid})

    def post(self, request, id_tavern, **kwargs):
        post_value = list(request.POST.keys())[1]

        if post_value == 'wait':
            Order.objects.filter(id = request.POST[post_value]).update(item_status = Order.item_stats[1])  

        if post_value == 'ready':
            Order.objects.filter(id = request.POST[post_value]).update(item_status = Order.item_stats[2])  

        place = get_object_or_404(Taverna, id = id_tavern)

        orders_for_place_wait = OrderItem.objects.all().filter(product__place__id = place.id, order__item_status = Order.item_stats[0])
        orders_for_place_ready = OrderItem.objects.all().filter(product__place__id = place.id, order__item_status = Order.item_stats[1])
        orders_for_place_paid = OrderItem.objects.all().filter(product__place__id = place.id, order__item_status = Order.item_stats[2])

        print(orders_for_place_wait.count())
        print(orders_for_place_ready.count())
        print(orders_for_place_paid.count())

        return render(request, "users/user_place_info.html", {'orders_wait':orders_for_place_wait,
                                                              'orders_ready':  orders_for_place_ready, 
                                                              'orders_paid': orders_for_place_paid})


