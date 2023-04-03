from django.db import models
# Create your models here.


class Driver(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)
    drivers_license =  models.CharField(max_length=50)
    identification_card = models.CharField(null=False, max_length=50, unique=True)
    model_vehicle = models.CharField(max_length=50)
    car_license_plate = models.CharField(max_length=50, unique=True)
    soat  =  models.CharField(max_length=50)
    driver_approved = models.BooleanField(null=True)
    date_created = models.DateField(auto_now_add=True)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    driver_active = models.BooleanField()
    city =  models.CharField(max_length=50, null=True)
    reference_point =  models.CharField(max_length=50, null=True)

    def __str__(self):
       return self.name







