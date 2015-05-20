from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Catelog(models.Model):
	name=models.CharField(max_length=50,verbose_name='产品类型')
	
class Product(models.Model):
	SHOPURL=''
	product_name=models.CharField(max_length=50,verbose_name='产品名称')
	thumb_nail=models.ImageField(verbose_name='缩略图')
	shop_url=models.URLField(max_length=200,verbose_name='购买链接',default=SHOPURL)
	catelog=models.ForeignKey('Catelog')
	product_img=models.ImageField('产品图片')
	product_detail=RichTextField()
	
