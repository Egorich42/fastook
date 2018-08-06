#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views
from clients.models import Client

urlpatterns = [
    url(r'^(?P<id>\d+)/$', views.show_user_profile, name='detali'),
    url(r'^(?P<id>\d+)/orders/(?P<id_tavern>\d+)$', views.show_tavern_orders, name='show_tavern_orders'),

]
