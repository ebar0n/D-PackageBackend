from django.conf.urls import url
from sw_vehicles.api import GetModelView, GetPackageTypeView, GetShipmentTypeView, GetVehicleCategoryView

urlpatterns = [
    url(r'^getpackagetype/$', GetPackageTypeView.as_view(), name='getpackagetype'),
    url(r'^getvehiclecategory/$', GetVehicleCategoryView.as_view(), name='getvehiclecategory'),
    url(r'^getmodel/$', GetModelView.as_view(), name='getmodel'),
    url(r'^getshipmenttype/$', GetShipmentTypeView.as_view(), name='getshipmenttype'),
]
