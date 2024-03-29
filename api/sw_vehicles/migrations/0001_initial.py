# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-23 03:13
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Modelo de vehiculo',
                'verbose_name_plural': 'Modelo de vehiculo',
            },
        ),
        migrations.CreateModel(
            name='PackageType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('description', models.CharField(max_length=100, verbose_name='Descripción')),
                ('codename', models.CharField(max_length=100, verbose_name='Codigo')),
                ('weight_min', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Peso minimo')),
                ('weight_max', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Peso maximo')),
                ('height_min', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Altura minimo')),
                ('height_max', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Altura maximo')),
                ('width_min', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Anchura minimo')),
                ('width_max', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Anchura maximo')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Tipo de paquete',
                'verbose_name_plural': 'Tipos de paquetes',
            },
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_plate', models.CharField(max_length=100, verbose_name='Nombre')),
                ('photo1', models.ImageField(blank=True, upload_to='vehiculePhoto', verbose_name='Foto')),
                ('photo2', models.ImageField(blank=True, upload_to='vehiculePhoto', verbose_name='Foto')),
                ('photo3', models.ImageField(blank=True, upload_to='vehiculePhoto', verbose_name='Foto')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Vehiculo',
                'verbose_name_plural': 'Vehiculos',
            },
        ),
        migrations.CreateModel(
            name='VehicleCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('description', models.CharField(max_length=100, verbose_name='Descripción')),
                ('codename', models.CharField(max_length=100, verbose_name='Codigo')),
                ('icon', models.CharField(max_length=100, verbose_name='Icono')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('packagetype', models.ManyToManyField(
                    blank=True,
                    to='sw_vehicles.PackageType',
                    verbose_name='Tipos de paquete')),
            ],
            options={
                'verbose_name': 'Categoria de vehiculo',
                'verbose_name_plural': 'Categorias de vehiculo',
            },
        ),
        migrations.AddField(
            model_name='vehicle',
            name='category',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='sw_vehicles.VehicleCategory',
                verbose_name='Categoria'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='model',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='sw_vehicles.Model',
                verbose_name='Modelo'),
        ),
    ]
