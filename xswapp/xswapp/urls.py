from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'xswapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')), 
    
    url(r'^polls/',include('xswtest.urls',namespace='xswtest')),
    url(r'^sendmail/',include('sendmail.urls',namespace='sendmail')),	
    url(r'^user/',include('register.urls',namespace='user')),
    
    url(r'^ckeditor/', include('ckeditor.urls')),   
    url(r'^chaining/', include('smart_selects.urls')),
    url(r'^admin/', include(admin.site.urls)),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
