# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-18 14:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sw_payments', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bank',
            options={'verbose_name': 'bank', 'verbose_name_plural': 'banks'},
        ),
        migrations.AlterModelOptions(
            name='bankaccount',
            options={'verbose_name': 'bank account', 'verbose_name_plural': 'bank accounts'},
        ),
        migrations.AlterField(
            model_name='bank',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='bank',
            name='name',
            field=models.CharField(max_length=100, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='bank',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='updated at'),
        ),
        migrations.AlterField(
            model_name='bankaccount',
            name='bank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sw_payments.Bank', verbose_name='bank'),
        ),
        migrations.AlterField(
            model_name='bankaccount',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='bankaccount',
            name='holder',
            field=models.CharField(max_length=100, verbose_name='holder'),
        ),
        migrations.AlterField(
            model_name='bankaccount',
            name='identity_card',
            field=models.CharField(max_length=8, verbose_name='identity card'),
        ),
        migrations.AlterField(
            model_name='bankaccount',
            name='number',
            field=models.CharField(max_length=20, verbose_name='number'),
        ),
        migrations.AlterField(
            model_name='bankaccount',
            name='type',
            field=models.IntegerField(choices=[[1, 'Saving'], [2, 'Common']], verbose_name='type'),
        ),
        migrations.AlterField(
            model_name='bankaccount',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='updated at'),
        ),
    ]
