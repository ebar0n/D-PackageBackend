from django.conf.urls import url
from sw_vehicles.api import GetDataView

urlpatterns = [
    url(r'^getdata/$', GetDataView.as_view(), name='getdata'),
]
