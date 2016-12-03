from django.utils.translation import ugettext as _
from rest_framework import generics, status, viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response
from sw_shipments.models import Shipment, Status
from sw_shipments.serializers import ConfirmShipmentSerializer, ShipmentSerializer
from sw_users import mixins as mixins


class ShipmentViewSet(mixins.ClientCRUDPermissions, viewsets.ModelViewSet):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer

    @list_route(methods=['post'])
    def confirm_shipment(self, request, *args, **kwargs):
        serializer = ConfirmShipmentSerializer(
            data=request.data
        )
        if not serializer.is_valid():
            return Response({'errors': serializer.errors}, status.HTTP_400_BAD_REQUEST)

        data = serializer.data

        try:
            shipment = Shipment.objects.get(pk=data.get('id'))
        except Shipment.DoesNotExist:
            return Response({
                'status': 'Not Found',
                'message': _('Shipment does not exist.')
            }, status.HTTP_404_NOT_FOUND)

        if data.get('confirm'):
            codename = 'status_requested'
        else:
            codename = 'status_canceled'

        shipment.status = Status.objects.get(codename=codename)
        shipment.save(update_fields=['status'])

        return Response({}, status.HTTP_200_OK)


class InboxShipmentView(generics.ListAPIView):
    queryset = Shipment.objects.filter(status__codename='status_requested')
    serializer_class = ShipmentSerializer
