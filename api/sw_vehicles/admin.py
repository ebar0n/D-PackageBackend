from django.contrib.gis import admin
from sw_vehicles.models import Model, PackageType, VehicleCategory


@admin.register(PackageType)
class PackageTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'codename')
    list_filter = ('price',)
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('name', 'codename')


@admin.register(VehicleCategory)
class VehicleCategoryAdmin(admin.ModelAdmin):
    filter_horizontal = ('packagetype',)
    list_display = ('name', 'codename')
    list_filter = ('packagetype',)
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('name', 'codename')


@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('name',)
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('name',)
