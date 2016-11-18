# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-18 14:15
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sw_shipments', '0004_auto_20161113_1917'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='metric',
            options={'verbose_name': 'metric', 'verbose_name_plural': 'metrics'},
        ),
        migrations.AlterModelOptions(
            name='shipment',
            options={'verbose_name': 'shipment', 'verbose_name_plural': 'shipment'},
        ),
        migrations.AlterModelOptions(
            name='shipmenttype',
            options={'verbose_name': 'shipment type', 'verbose_name_plural': 'shipment types'},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name': 'estado', 'verbose_name_plural': 'estado'},
        ),
        migrations.AddField(
            model_name='metric',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='created at'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='metric',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='updated at'),
        ),
        migrations.AddField(
            model_name='reputation',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='created at'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reputation',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='updated at'),
        ),
        migrations.AddField(
            model_name='status',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='created at'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='status',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='updated at'),
        ),
        migrations.AlterField(
            model_name='metric',
            name='name',
            field=models.CharField(max_length=100, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='metric',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='value'),
        ),
        migrations.AlterField(
            model_name='reputation',
            name='commentary',
            field=models.TextField(verbose_name='commentary'),
        ),
        migrations.AlterField(
            model_name='reputation',
            name='score',
            field=models.PositiveSmallIntegerField(verbose_name='score'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sw_users.ClientAccount', verbose_name='client'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='destination',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326, verbose_name='destination'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='insured_value',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='insured value'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='origin',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326, verbose_name='origin'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='packagetype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sw_vehicles.PackageType', verbose_name='package type'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='photo1',
            field=models.ImageField(blank=True, upload_to='shipmentPhoto', verbose_name='photo 1'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='photo2',
            field=models.ImageField(blank=True, upload_to='shipmentPhoto', verbose_name='photo 2'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='photo3',
            field=models.ImageField(blank=True, upload_to='shipmentPhoto', verbose_name='photo 3'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='price'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='receiver',
            field=models.CharField(max_length=100, verbose_name='receiver'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='reputation',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sw_shipments.Reputation', verbose_name='reputation'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sw_users.ServiceAccount', verbose_name='service provider'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='shipmenttype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sw_shipments.ShipmentType', verbose_name='shipment type'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sw_shipments.Status', verbose_name='estado'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='tags',
            field=models.CharField(max_length=100, verbose_name='tags'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='updated at'),
        ),
        migrations.AlterField(
            model_name='shipmenttype',
            name='codename',
            field=models.CharField(max_length=100, verbose_name='nombre en código'),
        ),
        migrations.AlterField(
            model_name='shipmenttype',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='shipmenttype',
            name='description',
            field=models.TextField(max_length=200, verbose_name='descripción'),
        ),
        migrations.AlterField(
            model_name='shipmenttype',
            name='icon',
            field=models.CharField(max_length=100, verbose_name='icon'),
        ),
        migrations.AlterField(
            model_name='shipmenttype',
            name='insured_value',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='insured value'),
        ),
        migrations.AlterField(
            model_name='shipmenttype',
            name='name',
            field=models.CharField(max_length=100, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='shipmenttype',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='price'),
        ),
        migrations.AlterField(
            model_name='shipmenttype',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='updated at'),
        ),
        migrations.AlterField(
            model_name='status',
            name='codename',
            field=models.CharField(max_length=100, verbose_name='nombre en código'),
        ),
        migrations.AlterField(
            model_name='status',
            name='name',
            field=models.CharField(max_length=100, verbose_name='nombre'),
        ),
    ]
