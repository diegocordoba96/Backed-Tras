from django.shortcuts import render
from .models import Driver
from Rider.models import Rider
from general.locations import get_location


# Create your views here.
def post_locations_driver(data):
    id = data['id']
    city = data['city']
    reference_point = data['reference_point']
    location = get_location(reference_point,city)
    Driver.objects.filter(id=id).update(latitude=location['latitude'], longitude=location['longitude'])
    print('location update in driver',id)

        
def post_locations_rider(data):
    id = data['id']
    city = data['city']
    reference_point = data['reference_point']
    location = get_location(reference_point,city)
    Rider.objects.filter(id=id).update(latitude=location['latitude'], longitude=location['longitude'])
    print('location update in rider',id)



