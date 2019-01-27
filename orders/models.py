from django.db import models
from taverns.models import Product, Taverna
import datetime
from django.conf import settings

from datetime import date
from django.utils import timezone

class Order(models.Model):
    item_stats = (('wait', 'Ожидает'),('ready','Готов'),('paid','Оплачен'))
    appointed_time = models.TimeField(default=datetime.time(16))
    created = models.DateTimeField(verbose_name='Создан', auto_now_add=True)
    item_status = models.CharField(max_length = 20, choices=item_stats, db_index=True, default = item_stats[0], verbose_name='статус заказа')

    class Meta:
        ordering = ('-created', )
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Заказ: {}'.format(self.id)
        pass

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
        pass




class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE,)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE,)
    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(verbose_name='Количество', default=1)
    sess_id = models.CharField(max_length = 320,  db_index=True,  verbose_name='Сессия')
    created_at = models.DateTimeField(default = timezone.now)


    def __str__(self):
        return '{}'.format(self.id)
        pass

    def get_cost(self):
        return self.price * self.quantity
        pass

    def get_absolute_url(self):
        return reverse('orders:detali', args=[str(self.id)])
        pass