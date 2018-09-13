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
from orders.models import OrderItem, Order

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


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


class OwnerProfile(ListView):
    @method_decorator(login_required)
    def get(self, request,id):
        user = get_object_or_404(User, id=id)
        taverns = Taverna.objects.filter(owner_id = user.id-1)  
        print(taverns[0].id)
        return render(request, 'users/user_profile.html', {'taverns':taverns})
        pass


class PostDetail(ListView):
    @method_decorator(login_required)
    def get(self, request,id,id_tavern):
        place = get_object_or_404(Taverna, id=id_tavern)
        orders_for_place_wait = OrderItem.objects.all().filter(product__place__id = place.id, order__item_status = Order.item_stats[0])
        orders_for_place_ready = OrderItem.objects.all().filter(product__place__id = place.id, order__item_status = Order.item_stats[1])
        orders_for_place_paid = OrderItem.objects.all().filter(product__place__id = place.id, order__item_status = Order.item_stats[2])

        return render(request, "users/user_place_info.html",{'orders_wait':orders_for_place_wait,
                                                              'orders_ready':  orders_for_place_ready, 
                                                              'orders_paid': orders_for_place_paid})

    def post(self, request, id_tavern, **kwargs):
        post_value = list(request.POST.keys())[1]
        status = Order.item_stats[1][0]

        if post_value == 'wait':
            status = Order.item_stats[1]

        if post_value == 'ready':
            status = Order.item_stats[2]

        chosen_order = Order.objects.filter(id = request.POST[post_value]).update(item_status = status)  


        place = get_object_or_404(Taverna, id=id_tavern)

        orders_for_place_wait = OrderItem.objects.all().filter(product__place__id = place.id, order__item_status = Order.item_stats[0])
        orders_for_place_ready = OrderItem.objects.all().filter(product__place__id = place.id, order__item_status = Order.item_stats[1])
        orders_for_place_paid = OrderItem.objects.all().filter(product__place__id = place.id, order__item_status = Order.item_stats[2])

        return render(request, "users/user_place_info.html",{'orders_wait':orders_for_place_wait,
                                                              'orders_ready':  orders_for_place_ready, 
                                                              'orders_paid': orders_for_place_paid})

