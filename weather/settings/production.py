from split_settings.tools import include

PRODUCTION_SETTINGS = [
    'base.py',
    'components/django_storages.py',
    'components/sentry.py',
]
include(*PRODUCTION_SETTINGS)

HOSTNAME = 'https://weather.com.ua'
DEBUG = False