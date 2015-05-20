from django.db import models

# Create your models here.
class Intro(models.Model):
	title=models.CharField(max_length=50,verbose_name='小狮王简介')
	intro=models.TextField(verbose_name='简介')
	models.DateField(auto_now=True)
	def __unicode__(self):
		return self.title
	class Meta:
		verbose_name = "小狮王简介"
