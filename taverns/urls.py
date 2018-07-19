#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.http import HttpResponse
from django.views.generic import TemplateView
from . import views
from taverns.views import *

from django.conf.urls import *


urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^(?P<slug>[-\w]+)/$', views.show_tavern, name='show_tavern'), 
    url(r'^articles/(?P<slug>[-\w]+)/$',  views.show_product, name='detail'),
]
