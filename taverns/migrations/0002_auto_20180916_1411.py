# Generated by Django 2.0.7 on 2018-09-16 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taverns', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(blank=True, db_index=True, verbose_name='Цена'),
        ),
    ]
