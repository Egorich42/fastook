from django.db import models
from django.urls import reverse
#from clients.models import Client
from geo import convert_adres, insert_cafe_from_fastook, dj_cafe_insert_cafes


# Create your models here.
class Taverna(models.Model):

    owner = models.ForeignKey('clients.Owner', related_name = 'owner', on_delete = models.CASCADE, verbose_name="владелец", default=1)
    icon = models.ImageField(upload_to='place_icons/', blank=True, verbose_name="Аватарка заведения", default = 'place_icons/default.png')
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название")

    city = models.CharField(max_length=200, db_index=True, verbose_name="Город", default ="")
    street = models.CharField(max_length=200, db_index=True, verbose_name="Улица", default ="")
    building = models.CharField(max_length=200, db_index=True, verbose_name="Дом", default ="")

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
        pass


    def get_absolute_url(self):
        return reverse('taverns:detali', args=[str(self.slug)])
        pass

    def full_adress(self):
        return 'Беларусь,{city}, {street},{build}'.format(city = self.city, street = self.street, build = self.building)
        pass
        
    def addres_to_coord(self):
        return convert_adres(self.full_adress())
        pass



    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        cafe_coords = convert_adres(self.full_adress())
        print(cafe_coords)
        insert_com = insert_cafe_from_fastook.format(
                                id = 3363+self.id+2222, 
                                name = "'"+self.name+"'", 
                                adr = "'"+self.full_adress()+"'",
                                lon = cafe_coords['longitude'],
                                lat = cafe_coords['latitude'], 
                                dj_id = self.id,
                                )

        dj_cafe_insert_cafes(insert_com) 

        return True
        pass




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