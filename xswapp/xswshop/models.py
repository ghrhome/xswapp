# -*- coding: utf-8 -*-
from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Catelog(models.Model):
    name = models.CharField(max_length=50, verbose_name='产品类型')
    version =models.CharField(max_length=20,verbose_name='商品类型版本')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "产品类型"
        verbose_name_plural = "产品类型"



class Product(models.Model):
    SHOPURL_TMALL = 'http://lion.tmall.com/category-367325168.htm?spm=a1z10.1-b.w9154402-9436601579.6.QIgjSC'
    SHOPURL_YHD = ''
    SHOPURL_JD = ''
    product_name = models.CharField(max_length=50, verbose_name='产品名称')
    background_color = models.CharField(max_length=20, verbose_name='背景颜色', default='#c5e1eb')
    sort_id = models.IntegerField(verbose_name='商品排序', default=1, blank=True)

    thumb_nail = models.ImageField(verbose_name='缩略图')
    title_img = models.ImageField(verbose_name='产品名称图片')
    shop_url_tmall = models.URLField(max_length=200, verbose_name='天猫购买链接', default=SHOPURL_TMALL, blank=True)
    shop_url_yhd = models.URLField(max_length=200, verbose_name='一号店购买链接', blank=True)
    shop_url_jd = models.URLField(max_length=200, verbose_name='京东购买链接', blank=True)
    catelog = models.ForeignKey('Catelog')
    product_img = models.ImageField('产品图片')
    product_detail = RichTextField()

 #   relation_product = models.ManyToManyField('self')
    bottom_left_product=models.ImageField(verbose_name='底部左侧图片',default='')
    bottom_left_link=models.URLField(verbose_name='底部左侧链接',default=SHOPURL_JD )
    bottom_right_product=models.ImageField(verbose_name='底部右侧图片',default='')
    bottom_right_link=models.URLField(verbose_name='底部右侧链接',default=SHOPURL_TMALL)
    share_info=models.CharField(max_length=200,verbose_name="分享信息",default='小狮王是由创始于1891年的日本狮王出品的，以超过120年的传承经验和领先科技，诚挚为您的孩子提供安全优质的口腔护理产品。',blank=True)
    version =models.CharField(max_length=20,verbose_name='商品版本',default='0.0.1')

    def __unicode__(self):
        return self.product_name

    class Meta:
        verbose_name = "产品"
        verbose_name_plural = "产品"

