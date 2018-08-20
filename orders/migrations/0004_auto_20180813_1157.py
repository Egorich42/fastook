# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-08-13 11:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20180813_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='item_status',
            field=models.CharField(choices=[('ожидает', 'wait'), ('готов', 'ready'), ('оплачен', 'paid')], db_index=True, default=('ожидает', 'wait'), max_length=20, verbose_name='статус заказа'),
        ),
    ]
