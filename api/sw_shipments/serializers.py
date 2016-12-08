from rest_framework import serializers
from sw_shipments.models import Shipment, Status
from sw_users.serializers import ClientAccountSerializer, ServiceAccountSerializer
from utils.functions_geos import calculate_price


class ShipmentSerializer(serializers.ModelSerializer):
    """
        Shipment Serializer
    """
    client = ClientAccountSerializer(read_only=True)
    service = ServiceAccountSerializer(read_only=True)

    class Meta:
        model = Shipment
        fields = (
            'id', 'client', 'service', 'shipmenttype', 'packagetype', 'photo1', 'photo2', 'photo3', 'tags',
            'receiver', 'origin', 'destination', 'insured', 'price', 'status'
        )
        read_only_fields = ('id', 'price', 'status')

    def create(self, validated_data):
        validated_data['client'] = self.context['request'].user.client
        validated_data['status'] = Status.objects.get(codename='status_pre_requested')

        shipment = Shipment.objects.create(**validated_data)
        shipment.price = calculate_price(shipment)
        shipment.save(update_fields=['price', 'updated_at'])
        return shipment


class ConfirmShipmentSerializer(serializers.Serializer):
    """
        ConfirmShipment Serializer
    """
    id = serializers.IntegerField()
    confirm = serializers.BooleanField()


class AcceptShipmentSerializer(serializers.Serializer):
    """
        AcceptShipment Serializer
    """
    id = serializers.IntegerField()
    service = serializers.IntegerField()


class UpdateShipmentSerializer(serializers.Serializer):
    """
        UpdateShipment Serializer
    """
    id = serializers.IntegerField()
    status = serializers.IntegerField()
