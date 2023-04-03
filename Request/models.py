from django.db import models
from Driver.models import Driver 
from Rider.models import Rider

# Create your models here.
class Request(models.Model):
    id_driver =  models.IntegerField(null=False, default=0)
    id_rider = models.IntegerField(null=False, default=0)
    requet_active  = models.BooleanField(null=True)
    requet_finalized  = models.BooleanField(null=True)
    ponit_start = models.CharField(max_length=50, null=True)
    ponit_finish = models.CharField(max_length=50, null=True)
    city =  models.CharField(max_length=50, null=True)
    time_travel = models.FloatField(null=True, default=0)
    distance_travel = models.FloatField(null=True, default=0)
    cost = models.FloatField(null=True, default=0)

    def __str__(self):
       return str(self.id)