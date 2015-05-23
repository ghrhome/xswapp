from django.conf.urls import patterns, url
from . import views

urlpatterns=[
        url(r'^$', views.products_all, name='product_all'),
	url(r'^product/(?P<product_id>[0-9]+)/$',views.getproduct,name='getproduct'),
	url(r'^update/$',views.shop_update,name='shop_update'),
]
