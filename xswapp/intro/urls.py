from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^$',views.intro,name='index'),
    url(r'^intro/$', views.intro, name='intro'),
    url(r'^intro/(?P<cur_version>[0-9]\.[0-9]\.[0-9])/$', views.update, name='update'),
]

