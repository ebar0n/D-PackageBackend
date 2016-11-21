from django.contrib.gis import admin

from sw_users import models


class AccountInline(admin.StackedInline):
    model = models.UserAccount
    min_num = 1


@admin.register(models.ClientAccount)
class SpeakerAdmin(admin.ModelAdmin):
    inlines = (AccountInline,)


@admin.register(models.ServiceAccount)
class ReviewerAdmin(admin.ModelAdmin):
    inlines = (AccountInline,)
