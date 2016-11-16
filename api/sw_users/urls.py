from django.conf.urls import include, url
from rest_framework import routers

from .api import ClientAccountViewSet, LoginView, LogoutView, ServiceAccountViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'client', ClientAccountViewSet)
router.register(r'service', ServiceAccountViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
]
