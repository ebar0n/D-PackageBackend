# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-23 00:53
from __future__ import unicode_literals

import django.contrib.postgres.fields.ranges
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sw_vehicles', '0004_auto_20161118_1415'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='model',
            options={'verbose_name': 'modelo de vehículo', 'verbose_name_plural': 'modelos de vehículos'},
        ),
        migrations.AlterModelOptions(
            name='packagetype',
            options={'verbose_name': 'yipo de paquete', 'verbose_name_plural': 'tipos de paquetes'},
        ),
        migrations.AlterModelOptions(
            name='vehicle',
            options={'verbose_name': 'vehículo', 'verbose_name_plural': 'vehículos'},
        ),
        migrations.AlterModelOptions(
            name='vehiclecategory',
            options={'verbose_name': 'categoría de vehículo', 'verbose_name_plural': 'categorías de vehículos'},
        ),
        migrations.AlterField(
            model_name='model',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='creado a las'),
        ),
        migrations.AlterField(
            model_name='model',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='actualizado a las'),
        ),
        migrations.AlterField(
            model_name='packagetype',
            name='codename',
            field=models.CharField(max_length=100, verbose_name='código'),
        ),
        migrations.AlterField(
            model_name='packagetype',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='creado a las'),
        ),
        migrations.AlterField(
            model_name='packagetype',
            name='height',
            field=django.contrib.postgres.fields.ranges.IntegerRangeField(verbose_name='altura'),
        ),
        migrations.AlterField(
            model_name='packagetype',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='precio'),
        ),
        migrations.AlterField(
            model_name='packagetype',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='actualizado a las'),
        ),
        migrations.AlterField(
            model_name='packagetype',
            name='weight',
            field=django.contrib.postgres.fields.ranges.IntegerRangeField(verbose_name='peso'),
        ),
        migrations.AlterField(
            model_name='packagetype',
            name='width',
            field=django.contrib.postgres.fields.ranges.IntegerRangeField(verbose_name='ancho'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sw_vehicles.VehicleCategory', verbose_name='categoria'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='creado a las'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='license_plate',
            field=models.CharField(max_length=7, verbose_name='placa'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sw_vehicles.Model', verbose_name='modelo'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='photo1',
            field=models.ImageField(blank=True, upload_to='vehiculePhoto', verbose_name='foto 1'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='actualizado a las'),
        ),
        migrations.AlterField(
            model_name='vehiclecategory',
            name='codename',
            field=models.CharField(max_length=100, verbose_name='código'),
        ),
        migrations.AlterField(
            model_name='vehiclecategory',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='creado a las'),
        ),
        migrations.AlterField(
            model_name='vehiclecategory',
            name='packagetype',
            field=models.ManyToManyField(blank=True, to='sw_vehicles.PackageType', verbose_name='yipo de paquete'),
        ),
        migrations.AlterField(
            model_name='vehiclecategory',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='actualizado a las'),
        ),
    ]
