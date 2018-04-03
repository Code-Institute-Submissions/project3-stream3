from django.conf.urls import url, include
from django.contrib import admin
from home.views import *
from products.views import listcoffee

from django.views import static
from django.views.static import serve
from django.conf import settings

from django.views.static import serve

from accounts import urls as urls_accounts
from products import urls as urls_products
from cart import urls as urls_cart
from reviews import urls as urls_reviews

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', listcoffee, name='listcoffee'),
    url(r'^products/', include(urls_products)),
    url(r'^about$', about, name='about'),
    url(r'^hours$', hours, name='hours'),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^cart/', include(urls_cart)),
    url(r'^reviews/', include(urls_reviews)),
]
