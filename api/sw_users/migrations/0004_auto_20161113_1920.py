# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-13 19:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sw_users', '0003_useraccount_stripe_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceaccount',
            name='balance',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=6, verbose_name='Saldo'),
        ),
    ]
