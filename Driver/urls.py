from django.urls import path
from general.api import  get_driver_all, get_driver_approved, get_driver_active, get_driver

urlpatterns = [
    path('driver_all/' ,get_driver_all, name ='all_driver'),
    path('driver_approved/' ,get_driver_approved, name ='driver_approved'),
    path('driver_active/' ,get_driver_active, name ='driver_active'),
    path('driver/<int:identification_card>/' ,get_driver, name ='driver'),
]