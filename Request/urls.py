from django.urls import path
from general.api import  request, request_active, finish_request

urlpatterns = [
   path('post_request/' ,request, name ='post_request'),
   path('request_active/' ,request_active, name ='request_active'),
   path('finalized_request/<id>/' ,finish_request, name ='finalized_request'),


]