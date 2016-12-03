from rest_framework import permissions, views
from rest_framework.response import Response
from sw_shipments.models import ShipmentType
from sw_vehicles.models import Model, PackageType, VehicleCategory


class GetPackageTypeView(views.APIView):

    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        base = {}
        base['packagetype'] = []

        for obj in PackageType.objects.all():
            json = {}
            json['id'] = obj.id
            json['value'] = obj.name
            base['packagetype'].append(json)
        return Response(base)


class GetVehicleCategoryView(views.APIView):

    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        base = {}
        base['vehiclecategory'] = []

        for obj in VehicleCategory.objects.all():
            json = {}
            json['id'] = obj.id
            json['value'] = obj.name
            base['vehiclecategory'].append(json)
        return Response(base)


class GetModelView(views.APIView):

    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        base = {}
        base['model'] = []

        for obj in Model.objects.all():
            json = {}
            json['id'] = obj.id
            json['value'] = obj.name
            base['model'].append(json)
        return Response(base)


class GetShipmentTypeView(views.APIView):

    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        base = {}
        base['shipmenttype'] = []

        for obj in ShipmentType.objects.all():
            json = {}
            json['id'] = obj.id
            json['value'] = obj.name
            base['shipmenttype'].append(json)
        return Response(base)
