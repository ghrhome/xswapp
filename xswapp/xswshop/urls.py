from django.conf.urls import patterns, url
from . import views

urlpatterns = [
    url(r'^$', views.products_all, name='products_all'),
    url(r'^product/(?P<product_id>[0-9]+)/$', views.getproduct, name='getproduct'),
    url(r'^product_update/(?P<cur_version>[0-9]\.[0-9]\.[0-9])/$', views.shop_update, name='shop_update'),
]

