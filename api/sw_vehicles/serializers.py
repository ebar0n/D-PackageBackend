from rest_framework import serializers

from .models import Vehicle


class VehicleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehicle
        fields = (
            'license_plate',
            'model',
            'category',
            'photo1',
            'photo2',
            'photo3')
