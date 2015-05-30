from django.conf.urls import url

from . import views

urlpatterns=[
        url(r'^ppt/$',views.latest_ppt,name='lastest_ppt'),
        url(r'^ppt/(?P<class_id>[0-9]+)/$',views.getppt,name='getppt'),
        url(r'^ppt/ppt_update/(?P<cur_version>[0-9]\.[0-9]\.[0-9])/$',views.ppt_update,name='ppt_update'),
        url(r'^ppt/share/$',views.ppt_share,name='ppt_update')
]

