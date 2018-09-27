# Generated by Django 2.1 on 2018-09-27 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taverns', '0002_auto_20180916_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='products/deafult.png', upload_to='products/', verbose_name='Изображение товара'),
        ),
        migrations.AlterField(
            model_name='taverna',
            name='icon',
            field=models.ImageField(blank=True, default='place_icons/default.png', upload_to='place_icons/', verbose_name='Аватарка заведения'),
        ),
    ]
