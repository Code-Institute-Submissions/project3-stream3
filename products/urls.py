from django.conf.urls import url, include
from .views import listcoffee, detailcoffee

urlpatterns = [
    url(r'^$', listcoffee, name='listcoffee'),
    url(r'^(\d+)$', detailcoffee, name='detailcoffee'),
]