# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-25 00:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(
                    default=False, help_text='Designates that this user has all permissions without explicitly '
                    'assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(max_length=50, verbose_name='first name')),
                ('last_name', models.CharField(max_length=50, verbose_name='last name')),
                ('is_active', models.BooleanField(default=False, verbose_name='is active')),
                ('is_staff', models.BooleanField(
                    default=False, help_text='can login to the django admin.', verbose_name='is staff')),
                ('reset_password_key', models.CharField(blank=True, editable=False, max_length=40)),
                ('reset_password_key_expires', models.DateTimeField(editable=False, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('groups', models.ManyToManyField(
                    blank=True, help_text='The groups this user belongs to. A user will get all permissions granted '
                    'to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group',
                    verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(
                    blank=True, help_text='Specific permissions for this user.', related_name='user_set',
                    related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'account',
            },
        ),
    ]
