from django.conf.urls import include, url
from rest_framework import routers
from sw_users.api import (
    CardViewSet, ClientAccountViewSet, LoginView, LogoutView, ServiceAccountViewSet, UserAccountViewSet,
)

# Routers provide an easy way of automatically determining the URL conf.
router = routers.SimpleRouter()
router.register(r'card', CardViewSet, 'cards')
router.register(r'client', ClientAccountViewSet)
router.register(r'service', ServiceAccountViewSet)
router.register(r'user', UserAccountViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
]
