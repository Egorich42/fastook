#! /usr/bin/env python
# -*- coding: utf-8 -*

import datetime
from django.db import migrations
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
#from taverns.models import Taverna


#https://simpleisbetterthancomplex.com/tutorial/2018/01/18/how-to-implement-multiple-user-types-with-django.html
statuses = (('owner', 'owner',),('cook', 'cook',))

class Owner(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE,)
    status = models.CharField(choices = statuses, default = statuses[0], max_length=200,)

    def __str__(self):
        return str(self.user.username)
        pass

    def get_absolute_url(self):
        return reverse('clients:owner_place', args = [str(self.user.id)])
        pass


class Cook(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE,)
    work_place = models.OneToOneField('taverns.Taverna', on_delete = models.CASCADE, default = 1)
    status = models.CharField(choices = statuses, default = statuses[0], max_length=200,)

    def __str__(self):
        return str('повар в '+self.work_place.name)
        pass

    def get_absolute_url(self):
        return reverse('clients:cook_place', args = [str(self.work_place.id)])
        pass
