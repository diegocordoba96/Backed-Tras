from rest_framework import serializers
from Driver.models import Driver
from Rider.models import Rider
from Request.models import Request

#change name to class
class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields =  '__all__'
    

class RiderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rider
        fields =  '__all__'
    


class RequetSerializerAll(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields =  '__all__'
     

class RequetSerealizer(serializers.Serializer):
    id_rider = serializers.IntegerField()
    requet_active = serializers.BooleanField()
    ponit_start = serializers.CharField()
    ponit_finish = serializers.CharField()
    city = serializers.CharField()


    def create(self, validated_data):
        return Request.objects.create(**validated_data)
    

class FinishRequetSerealizer(serializers.Serializer):
    time_travel = serializers.FloatField()


    def update(self, instance, validated_data):
        #instance.requet_active = validated_data.get('requet_active',instance.requet_active)
        #instance.requet_finalized = validated_data.get('requet_finalized')
        instance.time_travel = validated_data.get('time_travel')
        instance.save()
        return instance
        #return Request.objects.update(**validated_data)
