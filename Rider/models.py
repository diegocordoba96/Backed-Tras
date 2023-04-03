from django.db import models

class Rider(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    phone = models.CharField(max_length=15)
    date_created = models.DateField(auto_now_add=True)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    city =  models.CharField(max_length=50, null=True)
    reference_point =  models.CharField(max_length=50, null=True)


    def __str__(self):
       return self.name