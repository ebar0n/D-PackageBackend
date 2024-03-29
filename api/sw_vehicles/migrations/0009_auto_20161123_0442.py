# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-23 04:42
from __future__ import unicode_literals

import django.contrib.postgres.fields.ranges
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sw_vehicles', '0008_merge_20161123_0441'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='model',
            options={'verbose_name': 'vehicle model', 'verbose_name_plural': 'vehicle models'},
        ),
        migrations.AlterModelOptions(
            name='packagetype',
            options={'verbose_name': 'package type', 'verbose_name_plural': 'package types'},
        ),
        migrations.AlterModelOptions(
            name='vehicle',
            options={'verbose_name': 'vehicle', 'verbose_name_plural': 'vehicles'},
        ),
        migrations.AlterModelOptions(
            name='vehiclecategory',
            options={'verbose_name': 'vehicle category', 'verbose_name_plural': 'vehicle categories'},
        ),
        migrations.AlterField(
            model_name='model',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='model',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='updated at'),
        ),
        migrations.AlterField(
            model_name='packagetype',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='packagetype',
            name='height',
            field=django.contrib.postgres.fields.ranges.IntegerRangeField(verbose_name='height'),
        ),
        migrations.AlterField(
            model_name='packagetype',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='price'),
        ),
        migrations.AlterField(
            model_name='packagetype',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='updated at'),
        ),
        migrations.AlterField(
            model_name='packagetype',
            name='weight',
            field=django.contrib.postgres.fields.ranges.IntegerRangeField(verbose_name='weight'),
        ),
        migrations.AlterField(
            model_name='packagetype',
            name='width',
            field=django.contrib.postgres.fields.ranges.IntegerRangeField(verbose_name='width'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sw_vehicles.VehicleCategory', verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='license_plate',
            field=models.CharField(max_length=7, validators=[django.core.validators.RegexValidator('^.{7}$', 'El numero de placa debe ser de 7 caracteres')], verbose_name='license plate'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sw_vehicles.Model', verbose_name='model'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='photo1',
            field=models.ImageField(blank=True, upload_to='vehiculePhoto', verbose_name='photo 1'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='updated at'),
        ),
        migrations.AlterField(
            model_name='vehiclecategory',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='vehiclecategory',
            name='packagetype',
            field=models.ManyToManyField(blank=True, to='sw_vehicles.PackageType', verbose_name='package type'),
        ),
        migrations.AlterField(
            model_name='vehiclecategory',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='updated at'),
        ),
    ]
