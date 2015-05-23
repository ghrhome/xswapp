from django.conf.urls import url

from . import views


urlpatterns=[
#	url(r'^$',views.index,name='index'),
 	url(r'^test/$',views.test,name='test'),
	url(r'^getest/$',views.getest,name='gtest'),   
	url(r'^ppt/(?P<ppt_id>[0-9]+)/$',views.sendmail,name='sendmail'),
]
