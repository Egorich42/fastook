#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.LoginFormView.as_view()),
    url(r'^logout/$', views.LogoutView.as_view()),
    url(r'^(?P<id>\d+)/$', views.show_user_profile, name='show_user_profile'),
    url(r'^articles/(?P<id>\d+)/$', views.show_user_profile, name='show_user_profile'),
]
