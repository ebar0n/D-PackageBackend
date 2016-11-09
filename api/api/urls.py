# -*- coding: utf-8 -*-
# from django.conf import settings
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^api/v1/', include('accounts.urls')),
    # url(r'^static/(.*)$', django.views.static.serve, {'document_root': settings.STATIC_ROOT}),
    # url(r'^media/(.*)$', django.views.static.serve, {'document_root': settings.MEDIA_ROOT}),
]

# if settings.DOCS:
#     from rest_framework_swagger.views import get_swagger_view
#     swagger_view = get_swagger_view(title='API')
#     urlpatterns += [
#         url('^$', swagger_view),
#     ]
