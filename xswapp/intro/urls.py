from django.conf.urls import url

from . import views

urlpatterns=[
#       url(r'^$',views.index,name='index'),
        url(r'^intro/$',views.intro,name='intro'),
	url(r'^intro/update/$',views.update,name='update'),
]

