# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
from sw_shipments.models import Status


def MigrateDataAll(apps, schema_editor):

    Status.objects.get_or_create(
        name='Pre solicitado',
        codename='status_pre_requested'
    )

    Status.objects.get_or_create(
        name='Solicitado',
        codename='status_requested'
    )

    Status.objects.get_or_create(
        name='Aceptado',
        codename='status_accepted'
    )

    Status.objects.get_or_create(
        name='Retirado',
        codename='status_retired'
    )

    Status.objects.get_or_create(
        name='Entregado',
        codename='status_delivered'
    )

    Status.objects.get_or_create(
        name='Cancelado',
        codename='status_canceled'
    )


class Migration(migrations.Migration):

    dependencies = [
        ('sw_shipments', '0011_auto_20161130_2326'),
    ]

    operations = [
        migrations.RunPython(MigrateDataAll),
    ]
