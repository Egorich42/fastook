#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.utils.encoding import python_2_unicode_compatible
from django.contrib import admin
from .models import Taverna, Product


class TavernaAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'owner']
    prepopulated_fields = {'slug': ('name', )}


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price','place']
    list_editable = ['price']
    prepopulated_fields = {'slug': ('name', )}



admin.site.register(Taverna, TavernaAdmin)
admin.site.register(Product, ProductAdmin)
