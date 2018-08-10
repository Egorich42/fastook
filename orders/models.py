from django.db import models
from taverns.models import Product, Taverna
import datetime

class Order(models.Model):
    appointed_time = models.TimeField(default=datetime.time(16))
    created = models.DateTimeField(verbose_name='Создан', auto_now_add=True)
    paid = models.BooleanField(verbose_name='Оплачен', default=False)

    class Meta:
        ordering = ('-created', )
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Заказ: {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE,)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE,)
    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(verbose_name='Количество', default=1)

    def generate_mark(self):
        if self.quantity <= 9:
            self.quantity = '0{}'.format(self.quantity)

        if self.product.id <= 9:
            self.product.id = '0{}'.format(self.product.id)

        if self.product.place.id <= 9:
            self.product.place.id = '0{}'.format(self.product.place.id)

        return '{}{}{}{}'.format(self.id, self.product.place.id, self.product.id, self.quantity)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity

    def get_absolute_url(self):
        return reverse('orders:detali', args=[str(self.id)])