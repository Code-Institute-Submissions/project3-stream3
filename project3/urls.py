from django.conf.urls import url
from django.contrib import admin
from home.views import *
from products.views import listcoffee

from django.views import static
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', listcoffee, name='listcoffee'),
    url(r'^about$', about, name='about'),
    url(r'^hours$', hours, name='hours'),
]
