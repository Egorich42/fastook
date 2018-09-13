#! /usr/bin/env python
# -*- coding: utf-8 -*
from django.shortcuts import render, get_object_or_404, render_to_response
from django.views.generic.edit import FormView
from django.views.generic.base import View
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from taverns.models import Taverna
from orders.models import OrderItem, Order


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "login.html"
    success_url = "/"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")






def show_user_profile(request,id, **kwargs):
    user = get_object_or_404(User, id=id)
    if user == request.user or user.username == 'egor' or user.id == 1:
        taverns = Taverna.objects.filter(owner_id = user.id-1)  
        return render(request, 'users/user_profile.html', {'taverns':taverns})
        pass
    else:
        return render(request, "singles/clients/office_login_error.html")

    pass

def show_tavern_orders(request,id, id_tavern):
    user = get_object_or_404(User, id=id) 

    if user == request.user or user.username == 'egor' or user.id == 1:
        place = get_object_or_404(Taverna, id=id_tavern)
        if request.method == 'POST':


            post_value = list(request.POST.keys())[1]

            if post_value == 'wait':
                Order.objects.filter(id = request.POST[post_value]).update(item_status = Order.item_stats[1])

            if post_value == 'ready':
                Order.objects.filter(id = request.POST[post_value]).update(item_status = Order.item_stats[2])



            return render(request, "users/user_place_info.html")
        else:    
            orders_for_place_wait = OrderItem.objects.all().filter(product__place__id = place.id, order__item_status = Order.item_stats[0])
            orders_for_place_ready = OrderItem.objects.all().filter(product__place__id = place.id, order__item_status = Order.item_stats[1])
            orders_for_place_paid = OrderItem.objects.all().filter(product__place__id = place.id, order__item_status = Order.item_stats[2])

            print(len(orders_for_place_wait))
            print(len(orders_for_place_ready))
            print(len(orders_for_place_paid))



            return render(request, "users/user_place_info.html", {'orders_wait':orders_for_place_wait,
                                                              'orders_ready':  orders_for_place_ready, 
                                                              'orders_paid': orders_for_place_paid})

    else:
        return render(request, "singles/clients/office_login_error.html")
