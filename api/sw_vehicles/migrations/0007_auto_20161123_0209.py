# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-23 02:09
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sw_vehicles', '0006_auto_20161123_0209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='license_plate',
            field=models.CharField(max_length=7, validators=[django.core.validators.RegexValidator('^.{7}$', 'El numero de placa debe ser de 7 caracteres')], verbose_name='placa'),
        ),
    ]
