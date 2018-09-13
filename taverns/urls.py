#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.http import HttpResponse
from django.views.generic import TemplateView
from . import views
from taverns.views import *
from clients.views import LoginFormView, LogoutView
from django.conf.urls import *


urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^login/$',LoginFormView.as_view()),
    url(r'^logout/$',LogoutView.as_view()),
    url(r'^places/(?P<slug>[-\w]+)/$', views.show_tavern, name='detali'), 
    url(r'^products/(?P<slug>[-\w]+)/$',  views.show_product, name='detail'),
]