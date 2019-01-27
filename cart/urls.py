from django.conf.urls import url
from . import views
from cart.views import OrdersDeatil
urlpatterns = [
    url(r'^remove/(?P<product_id>\d+)/$', views.CartRemove, name='CartRemove'),
    url(r'^add/(?P<product_id>\d+)/$', views.CartAdd, name='CartAdd'),
    url(r'^$', views.CartDetail, name='CartDetail'),
    url(r'^my_current_orders/$', OrdersDeatil.as_view(), name='my_orders'),
]