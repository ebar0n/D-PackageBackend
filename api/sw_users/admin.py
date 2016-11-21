from django.contrib.gis import admin
from sw_users import models


class AccountInline(admin.StackedInline):
    model = models.UserAccount
    min_num = 1


@admin.register(models.ClientAccount)
class ClientAdmin(admin.ModelAdmin):
    inlines = (AccountInline,)


@admin.register(models.ServiceAccount)
class ServiceAdmin(admin.OSMGeoAdmin):
    inlines = (AccountInline,)
