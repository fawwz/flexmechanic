from django.db import models
from taggit.managers import TaggableManager
from django.contrib.gis.db import models as gis_models
# Create your models here.
from account.models import Mechanic

class Garage(gis_models.Model):
  mechanic = models.ForeignKey(Mechanic,on_delete=models.CASCADE)
  garage_id = models.AutoField(primary_key=True)
  garage_name = models.CharField(max_length=20)
  address = models.TextField()
  location = gis_models.PointField(null=True, blank=True)

  def __str__(self):
        return self.garage_name

class Services(models.Model):
  services_name = TaggableManager() 
  garage = models.ForeignKey(Garage,on_delete=models.CASCADE)

  def __str__(self):
        # return self.services_name
        tags = [str(tag) for tag in self.services_name.all()]
        return f"Services: {', '.join(tags)}"