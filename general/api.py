from rest_framework.decorators import api_view
from Driver.models import Driver 
from Rider.models import Rider
from Request.models import Request
from rest_framework.response import Response
from .serializers import DriverSerializer, RiderSerializer, RequetSerealizer, RequetSerializerAll, FinishRequetSerealizer
from  Driver.views import post_locations_driver, post_locations_rider
from rest_framework import status
from general.calculate_distance import get_distance
from .locations import get_location
from .calculate_cost import get_cost





#MODEL DRIVER
#get all driver
@api_view(['GET','POST'])
def get_driver_all(request):

    if request.method == 'GET':
        driver = Driver.objects.all()#.filter(driver_approved=True)
        driver_serializer = DriverSerializer(driver,many=True)
        return Response(driver_serializer.data, status = status.HTTP_200_OK)
    
    elif request.method == 'POST':
        driver_serializer = DriverSerializer(data = request.data)
        if driver_serializer.is_valid():
            driver_serializer.save()
            data = {
              'id': driver_serializer.data['id'],
              'city': driver_serializer.data['city'],
              'reference_point': driver_serializer.data['reference_point']
            }
            post_locations_driver(data)
            return Response(driver_serializer.data, status = status.HTTP_201_CREATED)
        return Response(driver_serializer.errors)
    

#get driver approved
@api_view(['GET'])
def get_driver_approved(request):

    if request.method == 'GET':
        driver = Driver.objects.all().filter(driver_approved=True)
        driver_serializer = DriverSerializer(driver,many=True)
        #post_locations(driver)
        return Response(driver_serializer.data, status = status.HTTP_200_OK)

#get driver active
@api_view(['GET'])
def get_driver_active(request):
    if request.method == 'GET':
        driver = Driver.objects.all().filter(driver_active=True)
        driver_serializer = DriverSerializer(driver,many=True)
        return Response(driver_serializer.data, status = status.HTTP_200_OK)
    
   
#get driver for identification_card
@api_view(['GET','PUT','DELETE'])
def get_driver(request,identification_card):
    driver = Driver.objects.filter(identification_card=identification_card).first()

    if driver:
        if request.method == 'GET':
            driver_serealizer = DriverSerializer(driver)
            return Response(driver_serealizer.data, status = status.HTTP_200_OK)
        
        elif request.method == 'PUT':
            driver_serealizer  = DriverSerializer(driver,data = request.data)
            if driver_serealizer.is_valid():
                driver_serealizer.save()
                return Response(driver_serealizer.data, status = status.HTTP_200_OK)
            return Response(driver_serealizer.errors, status = status.HTTP_400_BAD_REQUEST)
        
        elif request.method == 'DELETE':
            driver.delete()
            return Response({'message':'user delete succes!'},status = status.HTTP_200_OK)

    return Response({'message':'user does not exist'},status = status.HTTP_400_BAD_REQUEST) 


#MODEL RIDER
#get all rider
@api_view(['GET','POST'])
def get_rider_all(request):

    if request.method == 'GET':
        rider = Rider.objects.all()
        rider_serializer = RiderSerializer(rider,many=True)
        return Response(rider_serializer.data, status = status.HTTP_200_OK)
    
    elif request.method == 'POST':
        rider_serializer = RiderSerializer(data = request.data)
        if rider_serializer.is_valid():
            rider_serializer.save()
            data = {
              'id': rider_serializer.data['id'],
              'city': rider_serializer.data['city'],
              'reference_point': rider_serializer.data['reference_point']
            }
            post_locations_rider(data)
            return Response(rider_serializer.data, status = status.HTTP_201_CREATED)
        return Response(rider_serializer.errors) 



#MODEL RIDER
#get all rider
@api_view(['GET','POST'])
def get_rider_all(request):

    if request.method == 'GET':
        rider = Rider.objects.all()
        rider_serializer = RiderSerializer(rider,many=True)
        return Response(rider_serializer.data, status = status.HTTP_200_OK)
    
    elif request.method == 'POST':
        rider_serializer = RiderSerializer(data = request.data)
        if rider_serializer.is_valid():
            rider_serializer.save()
            data = {
              'id': rider_serializer.data['id'],
              'city': rider_serializer.data['city'],
              'reference_point': rider_serializer.data['reference_point']
            }
            post_locations_rider(data)
            return Response(rider_serializer.data, status = status.HTTP_201_CREATED)
        return Response(rider_serializer.errors) 



#MODEL REQUEST
#request
cont = 1000000000
@api_view(['GET','POST'])
def request(request):
    if request.method == 'GET':
        resquest = Request.objects.all()
        resquest_serializer = RequetSerializerAll(resquest,many=True)
        return Response(resquest_serializer.data, status = status.HTTP_200_OK)
    elif request.method == 'POST':
        test_data = {
            'id_rider': request.data['id_rider'],
            'requet_active': '1',
            'ponit_start': request.data['ponit_start'],
            'ponit_finish': request.data['ponit_finish'],
            'city': request.data['city'],
        }
        test_request = RequetSerealizer(data = test_data)
        if test_request.is_valid():
            test_request.save()
            #get distance betwen points
            data_ini = get_location(request.data['ponit_start'],request.data['city'])
            data_fin = get_location(request.data['ponit_finish'],request.data['city'])
            latitude_ini = data_ini['latitude']
            longitude_ini = data_ini['longitude']
            latitude_fin = data_fin['latitude']
            longitude_fin = data_fin['longitude']
            distance = get_distance(latitude_ini,longitude_ini,latitude_fin,longitude_fin)

            #Update distance en bd
            Request.objects.filter(id_rider=request.data['id_rider']).filter(ponit_start=request.data['ponit_start']).filter(ponit_finish=request.data['ponit_finish']).update(distance_travel=distance)

            #searching driver
            drivers = Driver.objects.all().filter(driver_active=True).filter(city=request.data['city'])
            for driver in drivers:
                latitude_rider = data_ini['latitude']
                longitude_rider = data_ini['longitude']
                data_driver = get_location(driver.reference_point,driver.city)
                latitude_driver = data_driver['latitude']
                longitude_driver = data_driver['longitude']
                distance = get_distance(latitude_rider,longitude_rider,latitude_driver,longitude_driver)
                if distance < cont:
                    #print('entre',driver.id)
                    driver_select = driver.id
                    Request.objects.filter(id_rider=request.data['id_rider']).filter(ponit_start=request.data['ponit_start']).filter(ponit_finish=request.data['ponit_finish']).update(id_driver=driver_select)
            return Response(test_request.data) 
        return Response(test_request.errors) 

@api_view(['GET'])
def request_active(request):
    if request.method == 'GET':
        resquest = Request.objects.all().filter(requet_active=True)
        resquest_serializer = RequetSerializerAll(resquest,many=True)
        return Response(resquest_serializer.data, status = status.HTTP_200_OK)


@api_view(['GET','PUT'])
def finish_request(request, id):
    if request.method == 'GET':
        resquest = Request.objects.all().filter(id=id)
        resquest_serializer = RequetSerializerAll(resquest,many=True)
        return Response(resquest_serializer.data, status = status.HTTP_200_OK)

    elif request.method == 'PUT':
        resquest = Request.objects.all().filter(id=id).first()
        request_serealizer  = RequetSerializerAll(resquest,data = request.data)
        if request_serealizer.is_valid():
            request_serealizer.save()
            cost = get_cost(request_serealizer['time_travel'].value,request_serealizer['distance_travel'].value)
            #Update cost en bd
            Request.objects.filter(id=id).update(cost=round(cost))
            return Response(request_serealizer.data, status = status.HTTP_200_OK)
        return Response(request_serealizer.errors, status = status.HTTP_400_BAD_REQUEST)


