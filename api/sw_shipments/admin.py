from django.contrib.gis import admin
from sw_shipments import models


@admin.register(models.ShipmentType)
class ShipmentTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'codename')
    list_filter = ('price',)
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('name', 'codename')


@admin.register(models.Status)
class StatusTypeAdmin(admin.ModelAdmin):
    pass
