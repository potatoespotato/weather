import os
import sys

from split_settings.tools import include

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.join(BASE_DIR, 'apps'))

from weather.settings.components.django_environ import env

base_settings = [
    # environ
    'components/django_environ.py',
    # common settings
    'components/django/installed_apps.py',
    'components/django/caches.py',
    'components/django/databases.py',
    'components/django/middleware.py',
    'components/django/templates.py',
    'components/django/validators.py',
    'components/django/extra_settings.py',
    'components/django/static.py',
    'components/django/media.py',
    'components/django/i18n.py',
    'components/django_rest_framework.py',
    # 'components/celery.py',
    # 'components/django-ckeditor.py',
    'components/django_cacheops.py',
    'components/versatile_image_field.py',
]

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

ROOT_URLCONF = 'weather.urls'

API_KEY = env('API_KEY')

WSGI_APPLICATION = 'weather.wsgi.application'

include(*base_settings)
