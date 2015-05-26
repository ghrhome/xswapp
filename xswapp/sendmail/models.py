# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Maillist(models.Model):
    title = models.CharField(max_length=50, verbose_name='邮件标题')
    body = models.TextField(verbose_name='邮件内容')
    mail_src = models.URLField(max_length=100, verbose_name='邮件资源地址')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "邮件下载"
        verbose_name_plural = "邮件下载"


class PPT(models.Model):
    title = models.CharField(max_length=50, verbose_name='PPT标题')
    ppt = models.FileField(verbose_name='PPT')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "PPT"
        verbose_name_plural = "PPT"
