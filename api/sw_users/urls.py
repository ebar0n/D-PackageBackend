from rest_framework import routers
from django.conf.urls import include, url

from .api import ClientAccountViewSet, ServiceAccountViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'client', ClientAccountViewSet)
router.register(r'service', ServiceAccountViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
