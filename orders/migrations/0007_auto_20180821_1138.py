# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-08-21 11:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_orderitem_item_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='item_status',
            new_name='sess_id',
        ),
    ]
