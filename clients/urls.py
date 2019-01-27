#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views
from clients.views import PostDetail, OwnerProfile,CookPlace

app_name = 'clients'


urlpatterns = [
    url(r'^(?P<id>\d+)$', OwnerProfile.as_view(), name='owner_place'),
    url(r'^cook_place/(?P<id>\d+)$', CookPlace.as_view(), name='cook_place'),

    url(r'^(?P<id>\d+)/orders/(?P<id_tavern>\d+)$', PostDetail.as_view())
]
