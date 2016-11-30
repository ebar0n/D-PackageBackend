from rest_framework import viewsets
from sw_shipments.models import Shipment
from sw_shipments.serializers import ShipmentSerializer
from sw_users import mixins


class ShipmentViewSet(mixins.ClientCRUDPermissions, viewsets.ModelViewSet):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer
