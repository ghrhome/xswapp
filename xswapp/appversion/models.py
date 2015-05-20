from django.db import models

# Create your models here.
class App_Version(models.Model):
	version=models.CharField(max_length==200,verbose_name='版本号')
	pub_date=models.DateTimeFiled(auto_now_add=True,verbose_name='添加日期')
	app_type=models.CharField(max_length=20,verbose_name='设备类型')
        app_url=models.URLField(max_length=200,verbose_name='下载链接')
	
	def __unicode__(self):
		return self.area_name
	class Meta:
		verbose_name="app版本"

