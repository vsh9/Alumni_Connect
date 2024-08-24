from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE','main.settings')

capp = Celery('main')
capp.conf.enable_utc = False

capp.conf.update(timezone = 'Asia/Kolkata')

capp.config_from_object(settings, namespace='CELERY')


capp.autodiscover_tasks()

@capp.task(bind = True)
def debug_task(self):
    print(f'Request: {self.request!r}')