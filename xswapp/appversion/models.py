from django.db import models

# Create your models here.
class App_Version(models.Model):
	version=models.CharField(max_length==200)
	pub_date=models.DateTimeFiled("date_published")
	app_type=models.CharField(max_length=20)
        app_url=models.CharField(max_length=200)


