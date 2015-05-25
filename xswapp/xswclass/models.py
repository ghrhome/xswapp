# -*- coding: utf-8 -*-
from django.db import models
# Create your models here.

class ClassName(models.Model):
        name=models.CharField(max_length=50,verbose_name='课程名称')
#       img=models.ImageField(width_field=480,verbose_name='广告页')
        url=models.URLField(max_length=100,verbose_name='PPT链接',blank=True)
#	ppt=models.FileField(verbose_name='PPT')
#	date=models.DateTimeField(auto_now=True)
	date=models.DateTimeField(verbose_name='上线日期')
        def __unicode__(self):
                return self.name
        class Meta:
        	verbose_name = "创建课程"

class ClassPage(models.Model):
        classname=models.ForeignKey('ClassName')
        img=models.ImageField(width_field=480,verbose_name='课程图片')
	update_date=models.DateTimeField(verbose_name='广告上线时间')
        def __unicode__(self):
                return self.classname
        class Meta:
                verbose_name = "添加课程图片"
