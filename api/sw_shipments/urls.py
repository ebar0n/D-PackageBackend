from django.conf.urls import include, url
from rest_framework import routers
from sw_shipments.api import InboxShipmentView, ShipmentViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.SimpleRouter()
router.register(r'shipment', ShipmentViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^inbox_shipment/', InboxShipmentView.as_view(), name='inbox_shipment'),
]
