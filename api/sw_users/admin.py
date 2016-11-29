from django.contrib.gis import admin
from sw_users import models
from django.utils.translation import ugettext as _


class AccountInline(admin.StackedInline):
    model = models.UserAccount
    min_num = 1


@admin.register(models.ClientAccount)
class ClientAdmin(admin.ModelAdmin):
    inlines = (AccountInline,)


@admin.register(models.ServiceAccount)
class ServiceAdmin(admin.OSMGeoAdmin):
    inlines = (AccountInline,)
    list_display = ('get_full_name', 'get_username', 'identity_card', 'phone', 'identity_check')
    list_editable = ('identity_check',)
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('useraccount__first_name', 'useraccount__last_name', 'useraccount__username' , 'identity_card',)

    def get_full_name(self, obj):
        return '{}'.format(obj.useraccount.get_full_name())

    def get_username(self, obj):
        return '{}'.format(obj.useraccount.username)

    get_full_name.short_description = _('full Name')
    get_username.short_description = _('username')
