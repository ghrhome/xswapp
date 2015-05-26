from django.conf.urls import patterns, url
from . import views

urlpatterns = [

    url(r'^register/parent/$', views.reg_parent, name='reg_parent'),
    url(r'^register/teacher/$', views.reg_teacher, name='reg_teacher'),
    url(r'^login/$', views.login, name='login'),
    url(r'^question/$', views.question, name='question'),
    url(r'^question/answer/$', views.answer, name='answer'),
    url(r'^update/parent/$', views.update_parent, name='update_parent'),
    url(r'^update/teacher/$', views.update_teacher, name='update_teacher'),
    url(r'^test/$', views.test, name='test'),
]
