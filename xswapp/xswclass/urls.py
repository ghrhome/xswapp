from django.conf.urls import url

from . import views

urlpatterns=[
#       url(r'^$',views.index,name='index'),
        url(r'^ppt/(?P<class_id>[0-9]+)/$',views.getppt,name='getppt'),
        url(r'^ppt/ppt_update/$',views.ppt_update,name='ppt_update'),
]

