#! /usr/bin/env python
# -*- coding: utf-8 -*

import datetime
from django.db import migrations
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    name = models.CharField(max_length=200, db_index=True, verbose_name='Название')
    rus_name = models.CharField(max_length=200, db_index=True, verbose_name='Название на русском')


    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('clients:detali', args=[str(self.user.id)])