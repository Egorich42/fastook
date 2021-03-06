from django.db import models
from django.urls import reverse
from clients.models import Client

# Create your models here.
class Taverna(models.Model):
    owner = models.ForeignKey(Client, related_name='owner', on_delete=models.CASCADE, verbose_name="владелец", default=1)
    icon = models.ImageField(upload_to='place_icons/', blank=True, verbose_name="Аватарка заведения", default = 'place_icons/default.png')
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    adres = models.CharField(max_length=200, db_index=True, verbose_name="Адрес")
    slug = models.SlugField(max_length=200, db_index=True,blank=True)
    work_time = models.CharField(max_length=200, db_index=True, verbose_name="Время работы")

    class Meta:
        ordering = ['name']
        index_together = [
            ['id', 'name', 'slug']
        ]
        verbose_name = 'Заведение'
        verbose_name_plural = 'Заведения'        

    def  __str__(self): 
        return str(self.name)


    def get_absolute_url(self):
        return reverse('taverns:detali', args=[str(self.slug)])




class Product(models.Model):
    place = models.ForeignKey(Taverna, related_name='products', on_delete=models.CASCADE, blank=True, verbose_name="Заведение")
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/', blank=True, verbose_name="Изображение товара",default = 'products/deafult.png')
    price = models.FloatField(db_index=True, blank=True, verbose_name="Цена")
    weight =  models.CharField(max_length=50, db_index=True, blank=True, verbose_name="Вес")
    description = models.TextField(blank=True, verbose_name="Описание")
   
    class Meta:
        ordering = ['name']
        index_together = [
            ['id', 'name', 'slug']
        ]
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return str(self.name)

        
    def get_absolute_url(self):
        return reverse('taverns:detail', args=[str(self.slug)])

#        http://dikiigrigorii.ru/blog/article/internet-magazin-na-django-stranica-zakazov-chast-6/19/