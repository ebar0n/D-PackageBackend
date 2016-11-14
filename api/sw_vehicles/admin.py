from django.contrib import admin

from .models import Model, PackageType, VehicleCategory


@admin.register(PackageType)
class PackageTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(VehicleCategory)
class VehicleCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    pass
