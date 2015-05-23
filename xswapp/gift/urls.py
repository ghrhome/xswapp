from django.conf.urls import url

from . import views

urlpatterns=[
#       url(r'^$',views.index,name='index'),
        url(r'^(?P<gift_id>[0-9]+)/$',views.getgift,name='getgift'),
        url(r'^update/$',views.gift_update,name='gift_update'),
	url(r'^reg/(?P<user_id>[0-9]+)/(?P<gift_id>[0-9]+)/$',views.gift_reg,name='gift_reg'),
]

