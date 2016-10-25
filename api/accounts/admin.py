# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext as _

from accounts import models


@admin.register(models.Account)
class AccountAdmin(admin.ModelAdmin):
    """
    AccountAdmin

    """
    fieldsets = (
        (None, {'fields': ('email',)}),
        (_('personal info'), {'fields': ('first_name', 'last_name',)}),
        (_('permissions info'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('dates info'), {'fields': ('last_login', 'created_at', 'updated_at',)}),
    )
    filter_horizontal = ('groups', 'user_permissions',)
    list_display = ('email', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_active', 'is_superuser', 'created_at')
    ordering = ('created_at',)
    readonly_fields = ('last_login', 'created_at', 'updated_at')
    search_fields = ('email',)
