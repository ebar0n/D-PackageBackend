# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import include, url
from django.contrib.gis import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include('sw_users.urls')),
]

if settings.DOCS:
    from rest_framework_swagger.views import get_swagger_view
    swagger_view = get_swagger_view(title='API')
    urlpatterns += [
        url(r'^$', swagger_view),
    ]
