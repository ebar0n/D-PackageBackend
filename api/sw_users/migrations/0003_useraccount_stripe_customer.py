# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-26 00:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sw_users', '0002_auto_20161025_2236'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='stripe_customer',
            field=models.CharField(blank=True, max_length=64, verbose_name='Stripe, customer ID'),
        ),
    ]
