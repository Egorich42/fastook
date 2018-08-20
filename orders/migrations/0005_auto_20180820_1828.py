# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-08-20 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20180813_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='item_status',
            field=models.CharField(choices=[('wait', 'Ожидает'), ('ready', 'Готов'), ('paid', 'Оплачен')], db_index=True, default=('wait', 'Ожидает'), max_length=20, verbose_name='статус заказа'),
        ),
    ]