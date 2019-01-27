#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from taverns.models import  Product
class DishCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "slug", "image", "price", "weight", "description"]




