# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-30 21:00
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sw_shipments', '0008_auto_20161123_0442'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='metric',
            options={'verbose_name': 'métrica', 'verbose_name_plural': 'métricas'},
        ),
        migrations.AlterModelOptions(
            name='shipment',
            options={'verbose_name': 'envío', 'verbose_name_plural': 'envío'},
        ),
        migrations.AlterModelOptions(
            name='shipmenttype',
            options={'verbose_name': 'tipo de envío', 'verbose_name_plural': 'tipos de envíos'},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name': 'status', 'verbose_name_plural': 'status'},
        ),
        migrations.AlterField(
            model_name='metric',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='creado a las'),
        ),
        migrations.AlterField(
            model_name='metric',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='actualizado a las'),
        ),
        migrations.AlterField(
            model_name='metric',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='valor'),
        ),
        migrations.AlterField(
            model_name='reputation',
            name='commentary',
            field=models.TextField(verbose_name='comentario'),
        ),
        migrations.AlterField(
            model_name='reputation',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='creado a las'),
        ),
        migrations.AlterField(
            model_name='reputation',
            name='score',
            field=models.PositiveSmallIntegerField(verbose_name='puntuación'),
        ),
        migrations.AlterField(
            model_name='reputation',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='actualizado a las'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sw_users.ClientAccount', verbose_name='cliente'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='creado a las'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='destination',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326, verbose_name='destino'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='insured_value',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='valor asegurado'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='origin',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326, verbose_name='origen'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='packagetype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sw_vehicles.PackageType', verbose_name='yipo de paquete'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='photo1',
            field=models.ImageField(blank=True, upload_to='shipmentPhoto', verbose_name='foto 1'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='photo2',
            field=models.ImageField(blank=True, upload_to='shipmentPhoto', verbose_name='foto 2'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='photo3',
            field=models.ImageField(blank=True, upload_to='shipmentPhoto', verbose_name='foto 3'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='precio'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='receiver',
            field=models.CharField(max_length=100, verbose_name='receptor'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='reputation',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='sw_shipments.Reputation', verbose_name='reputación'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sw_users.ServiceAccount', verbose_name='proveedor de servicio'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='shipmenttype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sw_shipments.ShipmentType', verbose_name='tipo de envío'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sw_shipments.Status', verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='tags',
            field=models.CharField(max_length=100, verbose_name='etiquetas'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='actualizado a las'),
        ),
        migrations.AlterField(
            model_name='shipmenttype',
            name='codename',
            field=models.CharField(max_length=100, unique=True, verbose_name='código'),
        ),
        migrations.AlterField(
            model_name='shipmenttype',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='creado a las'),
        ),
        migrations.AlterField(
            model_name='shipmenttype',
            name='insured_value',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='valor asegurado'),
        ),
        migrations.AlterField(
            model_name='shipmenttype',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='precio'),
        ),
        migrations.AlterField(
            model_name='shipmenttype',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='actualizado a las'),
        ),
        migrations.AlterField(
            model_name='status',
            name='codename',
            field=models.CharField(max_length=100, verbose_name='código'),
        ),
        migrations.AlterField(
            model_name='status',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='creado a las'),
        ),
        migrations.AlterField(
            model_name='status',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='actualizado a las'),
        ),
    ]