from rest_framework import serializers
from sw_shipments.models import Shipment, Status
from utils.functions_geos import calculate_price


class ShipmentSerializer(serializers.ModelSerializer):
    """
        Shipment Serializer
    """

    class Meta:
        model = Shipment
        fields = (
            'client', 'shipmenttype', 'packagetype', 'photo1', 'photo2', 'photo3', 'tags', 'receiver', 'origin',
            'destination', 'insured', 'price'
        )
        read_only_fields = ('client', 'price')

    def create(self, validated_data):
        validated_data['client'] = self.context['request'].user.client
        validated_data['status'] = Status.objects.get(codename='status_pre_requested')

        shipment = Shipment.objects.create(**validated_data)
        shipment.price = calculate_price(shipment)
        shipment.save(update_fields=['price', 'updated_at'])
        return shipment
