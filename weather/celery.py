import os
from celery import Celery
from manage import DEFAULT_DJANGO_SETTINGS_MODULE
from django.conf import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', DEFAULT_DJANGO_SETTINGS_MODULE)

# pylint-ignore
app = Celery('weather')
CELERY_TIMEZONE = settings.TIME_ZONE
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
