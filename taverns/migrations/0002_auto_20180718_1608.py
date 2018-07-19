# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-07-18 16:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taverns', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='place',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='taverns.Taverna', verbose_name='Заведение'),
        ),
        migrations.AlterField(
            model_name='taverna',
            name='icon',
            field=models.ImageField(blank=True, upload_to='place_icons/', verbose_name='Аватарка заведения'),
        ),
    ]
