# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-13 19:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sw_shipments', '0003_auto_20161026_0201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reputation',
            name='score',
            field=models.PositiveSmallIntegerField(verbose_name='Puntuacion'),
        ),
        migrations.AlterField(
            model_name='shipmenttype',
            name='description',
            field=models.TextField(max_length=200, verbose_name='Descripción'),
        ),
    ]
