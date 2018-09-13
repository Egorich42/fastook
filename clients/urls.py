#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views
from clients.models import Client
from clients.views import PostDetail, OwnerProfile

urlpatterns = [
    url(r'^(?P<id>\d+)$', OwnerProfile.as_view(), name='detali'),
    url(r'^(?P<id>\d+)/orders/(?P<id_tavern>\d+)$', PostDetail.as_view())
]
