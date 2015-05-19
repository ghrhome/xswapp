from django.db import models

# Create your models here.

class AsAreas(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    parent_id = models.IntegerField()
    area_name = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=6)

    def __unicode__(self):
        return self.area_name
    class Meta:
        managed = False
        db_table = 'as_areas'
