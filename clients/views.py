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
from orders.models import OrderItem


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
        orders_for_place = OrderItem.objects.all().filter(product__place__id = place.id)

        return render(request, "users/user_place_info.html",{'orders':orders_for_place})

    else:
        return render(request, "singles/clients/office_login_error.html")
