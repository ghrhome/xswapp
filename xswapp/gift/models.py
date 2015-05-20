from django.db import models

# Create your models here.

class Gift(models.Model):
	name=models.CharField(max_length=50,verbose_name='福利名称')
#	img=models.ImageField(width_field=480,verbose_name='广告页')
	date=models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.name
	class Meta:
		verbose_name = "福利"

class GiftItem(models.Model):
	gift=models.ForeignKey('Gift')
	img=models.ImageField(width_field=480,verbose_name='广告页')

	img_url=models.URLField(max_length=100,verbose_name='促销链接')
