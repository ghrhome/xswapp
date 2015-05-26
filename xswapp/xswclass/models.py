# -*- coding: utf-8 -*-
from django.db import models
# Create your models here.

class PPTName(models.Model):
    name = models.CharField(max_length=50, verbose_name='课程名称')
    # img=models.ImageField(width_field=480,verbose_name='广告页')
    url = models.URLField(max_length=100, verbose_name='PPT链接', blank=True)
    #	ppt=models.FileField(verbose_name='PPT')
    #	date=models.DateTimeField(auto_now=True)
    date = models.DateTimeField(verbose_name='上线日期')
    version= models.CharField(max_length=20,verbose_name='ppt版本')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "创建课程"


class PPTPage(models.Model):
    pptname = models.ForeignKey('PPTName')
    img = models.ImageField(verbose_name='课程图片')
    update_date = models.DateTimeField(verbose_name='广告上线时间')
    sort_id=models.IntegerField(verbose_name='页面排序')

    def __unicode__(self):
        return 'ppt'+'-'+str(self.sort_id)

    class Meta:
        verbose_name = "添加课程图片"
