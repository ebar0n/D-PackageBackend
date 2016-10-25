# -*- coding: utf-8 -*-
from __future__ import absolute_import

import os

from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
if not settings.configured:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')

# set the default Django settings module for the 'celery' program.
app = Celery('api', include=['utils.tasks.emails'])

app.config_from_object('api.celeryconfig')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
