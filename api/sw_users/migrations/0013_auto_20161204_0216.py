# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-04 02:16
from __future__ import unicode_literals

import uuid

import django.contrib.gis.db.models.fields
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sw_users', '0012_auto_20161130_2100'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clientaccount',
            options={'verbose_name': 'client', 'verbose_name_plural': 'clients'},
        ),
        migrations.AlterModelOptions(
            name='serviceaccount',
            options={'verbose_name': 'service provider', 'verbose_name_plural': 'services provider'},
        ),
        migrations.AlterField(
            model_name='clientaccount',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='clientaccount',
            name='phone',
            field=models.CharField(max_length=11, validators=[django.core.validators.RegexValidator('^\\d{11}$', 'The telephone number must be 11 numbers long')], verbose_name='phone'),
        ),
        migrations.AlterField(
            model_name='clientaccount',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='updated at'),
        ),
        migrations.AlterField(
            model_name='serviceaccount',
            name='address',
            field=models.CharField(max_length=100, verbose_name='address'),
        ),
        migrations.AlterField(
            model_name='serviceaccount',
            name='balance',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=6, verbose_name='balance'),
        ),
        migrations.AlterField(
            model_name='serviceaccount',
            name='bankaccount',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='sw_payments.BankAccount', verbose_name='bank account'),
        ),
        migrations.AlterField(
            model_name='serviceaccount',
            name='birthdate',
            field=models.DateField(verbose_name='birthdate'),
        ),
        migrations.AlterField(
            model_name='serviceaccount',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='serviceaccount',
            name='driver_license',
            field=models.ImageField(blank=True, upload_to='license', verbose_name="driver's license"),
        ),
        migrations.AlterField(
            model_name='serviceaccount',
            name='identity_card',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(999999999)], verbose_name='identity card'),
        ),
        migrations.AlterField(
            model_name='serviceaccount',
            name='identity_check',
            field=models.BooleanField(default=False, verbose_name='identity verified'),
        ),
        migrations.AlterField(
            model_name='serviceaccount',
            name='last_location_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last location date'),
        ),
        migrations.AlterField(
            model_name='serviceaccount',
            name='last_location_point',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326, verbose_name='last location point'),
        ),
        migrations.AlterField(
            model_name='serviceaccount',
            name='phone',
            field=models.CharField(max_length=11, validators=[django.core.validators.RegexValidator('^\\d{11}$', 'The telephone number must be 11 numbers long')], verbose_name='phone'),
        ),
        migrations.AlterField(
            model_name='serviceaccount',
            name='photo',
            field=models.ImageField(blank=True, upload_to='servicePhoto', verbose_name='photo'),
        ),
        migrations.AlterField(
            model_name='serviceaccount',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='updated at'),
        ),
        migrations.AlterField(
            model_name='serviceaccount',
            name='vehicle',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sw_vehicles.Vehicle', verbose_name='vehicle'),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='check_mail',
            field=models.BooleanField(default=False, verbose_name='check mail'),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='client',
            field=models.OneToOneField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='sw_users.ClientAccount', verbose_name='client'),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='service',
            field=models.OneToOneField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='sw_users.ServiceAccount', verbose_name='service provider'),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='token',
            field=models.UUIDField(default=uuid.uuid4, editable=False, null=True),
        ),
    ]
