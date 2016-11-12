from rest_framework import viewsets

from .serializers import ClientAccountSerializer, ServiceAccountSerializer
from .models import ClientAccount, ServiceAccount


class ClientAccountViewSet(viewsets.ModelViewSet):
    lookup_field = 'useraccount__username'
    queryset = ClientAccount.objects.all()
    serializer_class = ClientAccountSerializer


class ServiceAccountViewSet(viewsets.ModelViewSet):
    lookup_field = 'useraccount__username'
    queryset = ServiceAccount.objects.all()
    serializer_class = ServiceAccountSerializer
