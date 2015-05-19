# -*- coding: utf-8 -*-

from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.i
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Download(models.Model):
    download_title=models.CharField(max_length=100,verbose_name="下载标题")
    download_intro=RichTextField()
    download_src=models.FileField(max_length=200,verbose_name="下载资源")
#    category=models.ForeignKey(Category, verbose_name="主题分类")
   # subCategory=models.ForeignKey(SubCategory, verbose_name="子主题")
   # subCategory= ChainedForeignKey(SubCategory, chained_field="category", chained_model_field="category",verbose_name="子主题")
    download_num=models.IntegerField(default=0)
    def __unicode__(self):
        return self.download_title
    class Meta:
        verbose_name = "下载"
        verbose_name_plural = "下载"

class Hometown(models.Model):
    id=models.AutoField(primary_key=True)
    parent_id=models.IntegerField()
    area_name=models.CharField(max_length=50)
    zipcode=models.CharField(max_length=6)

 
