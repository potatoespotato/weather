
PRE_DJANGO_APPS = []

DJANGO_APPS = [
    'apps.main',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps'
]

PRE_VENDOR_APPS = []

VENDOR_APPS = [
    'widget_tweaks',
    'cacheops',
    'rest_framework',
    'solo',
    'favicon'
]

PRE_USER_APPS = []

USER_APPS = [
]

INSTALLED_APPS = PRE_DJANGO_APPS + DJANGO_APPS + PRE_VENDOR_APPS + VENDOR_APPS + PRE_USER_APPS + USER_APPS\

