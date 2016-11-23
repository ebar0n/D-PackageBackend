from rest_framework import serializers
from sw_vehicles.models import Vehicle


class VehicleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehicle
        fields = (
            'license_plate', 'model', 'category', 'color', 'photo1'
        )
