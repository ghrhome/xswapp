from django.conf.urls import patterns, url
from . import views,getxml

urlpatterns = [

    url(r'^register/parent/$', views.reg_parent, name='reg_parent'),
    url(r'^register/teacher/$', views.reg_teacher, name='reg_teacher'),
    url(r'^register/check/$', views.register_check, name='register_check'),
    url(r'^login/$', views.login, name='login'),
    url(r'^password/reset/$',views.passwd_reset,name='passwd_reset'),
    url(r'^password/lost/$',views.passwd_lost,name='passwd_lost'),
    url(r'^question/$', views.question, name='question'),
    url(r'^question/answer/$', views.answer, name='answer'),
    url(r'^update/parent/$', views.update_parent, name='update_parent'),
    url(r'^update/teacher/$', views.update_teacher, name='update_teacher'),
    url(r'^test/$', views.test, name='test'),
    url(r'^getxml/$',getxml.getxml,name='getxml'),

]
