from django.db import models

# Create your models here.

class ClassName(models.Model):
        name=models.CharField(max_length=50,verbose_name='课程名称')
#       img=models.ImageField(width_field=480,verbose_name='广告页')
        url=models.URLField(max_length=100,verbose_name='PPT链接')
	date=models.DateTimeField(auto_now=True)

        def __unicode__(self):
                return self.name
        class Meta:
                verbose_name = "创建课程"

class ClassPage(models.Model):
        classname=models.ForeignKey('ClassName')
        img=models.ImageField(width_field=480,verbose_name='课程图片')

        def __unicode__(self):
                return self.classname
        class Meta:
                verbose_name = "添加课程图片"
