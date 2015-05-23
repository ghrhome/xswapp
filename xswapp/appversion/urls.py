from django.conf.urls import url

from . import views

urlpatterns=[
#       url(r'^$',views.index,name='index'),
        url(r'^ios/$',views.ios_download,name='ios_download'),
        url(r'^android/$',views.android_download,name='android_download'),
	url(r'^ios/update/$',views.ios_update,name='ios_update'),
	url(r'^android/update/$',views.android_update,name='android_update'),
	url(r'^ios/check/$',views.ios_check,name='ios_check'),
	url(r'^android/check/$',views.android_check,name='android_check'),
]

