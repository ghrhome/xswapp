# -*- coding: utf-8 -*-
from django.db import models


# Create your models here.

class Gift(models.Model):
    name = models.CharField(max_length=50, verbose_name='福利名称')
    # img=models.ImageField(width_field=480,verbose_name='广告页')
    date = models.DateTimeField(auto_now=True)
    version =models.CharField(max_length=20,verbose_name='促销上线版本')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "福利"


class GiftItem(models.Model):
    gift = models.ForeignKey('Gift')
    title = models.CharField(max_length=50, verbose_name='标题')
    img = models.ImageField(verbose_name='广告页')
    img_url = models.URLField(max_length=100, verbose_name='促销链接')
    reg_user = models.BooleanField(default=False, verbose_name='注册限制')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "促销广告"


class GiftReg(models.Model):
    gift = models.ForeignKey('GiftItem')
    user = models.ForeignKey('register.User')
    username=models.CharField(max_length='20',verbose_name='用户姓名')
    user_phone=models.CharField(max_length="20",verbose_name='手机号码')
    date = models.DateTimeField(auto_now=True)
    received = models.BooleanField(default=False, verbose_name='已领取')

    def __unicode__(self):
        return self.gift

    class Meta:
        verbose_name = "礼品登记"
	
