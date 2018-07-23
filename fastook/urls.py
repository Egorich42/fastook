#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^cart/', include(('cart.urls','carts'), namespace='cart')),
    url(r'^orders/', include(('orders.urls','carts'), namespace='orders')),
    url(r'^clients/', include(('clients.urls','carts'), namespace='clients')),
    url(r'^', include(('taverns.urls','taverns'), namespace='taverns')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)