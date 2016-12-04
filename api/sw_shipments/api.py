from django.utils.translation import ugettext as _
from rest_framework import generics, permissions, status, viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response
from sw_shipments.models import Shipment, Status
from sw_shipments.serializers import (
    AcceptShipmentSerializer, ConfirmShipmentSerializer, ShipmentSerializer, UpdateShipmentSerializer
)
from sw_users.models import ServiceAccount


class ShipmentViewSet(viewsets.ModelViewSet):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        queryset = self.queryset
        if self.request.user.client:
            queryset.filter(client=self.request.user.client)
        elif self.request.user.service:
            queryset.filter(service=self.request.user.service)
        queryset.exclude(status__codename__in=['status_pre_requested', 'status_canceled'])
        return queryset

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

    @list_route(methods=['get'])
    def getstatus(self, request, *args, **kwargs):
        base = {}
        base['status'] = []

        for obj in Status.objects.all():
            json = {}
            json['id'] = obj.id
            json['value'] = obj.name
            base['status'].append(json)
        return Response(base)

    @list_route(methods=['post'])
    def accept_shipment(self, request, *args, **kwargs):
        serializer = AcceptShipmentSerializer(
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

        try:
            service = ServiceAccount.objects.get(pk=data.get('service'))
        except ServiceAccount.DoesNotExist:
            return Response({
                'status': 'Not Found',
                'message': _('ServiceAccount does not exist.')
            }, status.HTTP_404_NOT_FOUND)

        shipment.service = service
        shipment.status = Status.objects.get(codename='status_accepted')
        shipment.save(update_fields=['service', 'status'])
        return Response({}, status.HTTP_200_OK)

    @list_route(methods=['post'])
    def update_shipment(self, request, *args, **kwargs):
        serializer = UpdateShipmentSerializer(
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

        try:
            estatus = Status.objects.get(pk=data.get('status'))
        except Status.DoesNotExist:
            return Response({
                'status': 'Not Found',
                'message': _('Status does not exist.')
            }, status.HTTP_404_NOT_FOUND)

        shipment.status = estatus
        shipment.save(update_fields=['estatus'])
        return Response({}, status.HTTP_200_OK)


class InboxShipmentView(generics.ListAPIView):
    queryset = Shipment.objects.filter(status__codename='status_requested')
    serializer_class = ShipmentSerializer
    permission_classes = (permissions.IsAuthenticated,)
