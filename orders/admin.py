from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_field = ['product']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','appointed_time', 'created']
    list_filter = [ 'appointed_time',]
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)

#of9b63xk0o85sowwwik62ulloy1mbwhr