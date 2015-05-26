# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class string_with_title(str):
    def __new__(cls, value, title):
        instance = str.__new__(cls, value)
        instance._title = title
        return instance

    def title(self):
        return self._title

    __copy__ = lambda self: self
    __deepcopy__ = lambda self, memodict: self


class App_Version(models.Model):
    IOS = 'ios'
    ANDROID = 'android'
    APPTYPE = (
    (IOS, 'ios'),
    (ANDROID, 'android')
    )
    version = models.CharField(max_length=200, verbose_name='版本号')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='添加日期')
    app_type = models.CharField(max_length=20, choices=APPTYPE, verbose_name='设备类型')
    app_url = models.URLField(max_length=200, verbose_name='下载链接')

    def __unicode__(self):
        return self.app_type + ':' + self.version

    class Meta:
        verbose_name = "app版本"

# app_label = string_with_title("appversion", u"APP 版本")

