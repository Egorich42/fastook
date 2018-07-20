#! /usr/bin/env python
# -*- coding: utf-8 -*

import datetime
from datetime import date
from taverns.models import Taverna
from django.db import migrations
from django.db import models
from django.contrib.auth.models import User



class Client(models.Model):
    user = models.OneToOneField(User)
    place = models.ForeignKey(Taverna, related_name='places', on_delete=models.CASCADE, blank=True, verbose_name="Заведение")
    name = models.CharField(max_length=200, db_index=True, verbose_name='Название')
    rus_name = models.CharField(max_length=200, db_index=True, verbose_name='Название на русском')


