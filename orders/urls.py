#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.http import HttpResponse
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    url(r'^create/$', views.OrderCreate, name='OrderCreate')
]