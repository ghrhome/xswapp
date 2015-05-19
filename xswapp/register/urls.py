from django.conf.urls import patterns, url
from . import views

urlpatterns=[
#        url(r'^$',views.index,name='index'),
 # ex: /polls/5/
        url(r'^getjson/$', views.getAreaJson, name='getjson'),

]
