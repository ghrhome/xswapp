# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Intro(models.Model):
    title = models.CharField(max_length=50, verbose_name='小狮王简介')
    intro = models.TextField(verbose_name='简介')
    intro_img = models.ImageField(verbose_name='简介配图')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='添加日期')
    version=models.CharField(max_length=20, verbose_name='简介版本号')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "小狮王简介"
