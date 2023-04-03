from django.urls import path
from general.api import  get_rider_all

urlpatterns = [
    path('rider_all/' ,get_rider_all, name ='all_rider'),
  
]