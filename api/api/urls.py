# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view

swagger_view = get_swagger_view(title='API')

urlpatterns = [
    url(r'^docs/', swagger_view),
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include('sw_users.urls')),
]
