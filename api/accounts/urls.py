# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from rest_framework import routers

router = routers.SimpleRouter()

urlpatterns = [
    url(r'^', include(router.urls)),
]
