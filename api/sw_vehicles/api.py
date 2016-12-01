from rest_framework import permissions, views
from rest_framework.response import Response
from sw_shipments.models import ShipmentType
from sw_vehicles.models import Model, PackageType, VehicleCategory


class GetDataView(views.APIView):

    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        base = {}
        base['packagetype'] = {
            obj.id: obj.name
            for obj in PackageType.objects.all()
        }
        base['vehiclecategory'] = {
            obj.id: obj.name
            for obj in VehicleCategory.objects.all()
        }
        base['model'] = {
            obj.id: obj.name
            for obj in Model.objects.all()
        }
        base['shipmenttype'] = {
            obj.id: obj.name
            for obj in ShipmentType.objects.all()
        }
        return Response(base)
