from django.conf.urls import patterns, url
from . import views

urlpatterns=[
#        url(r'^$',views.index,name='index'),
 # ex: /polls/5/
        url(r'^getjson/$', views.getAreaJson, name='getjson'),
	url(r'^register/parent/$',views.regParent,name='reg_parent'),
	url(r'^register/teacher/$',views.regTeacher,name='reg_teacher'),
	url(r'^login/$',views.login,name='login'),
	url(r'^question/$',views.question,name='question'),
	url(r'^question/answer/$',views.answer,name='answer'),
	url(r'^update/$',views.update,name='update'),

	url(r'^test/$',views.test,name='test'),
]
