from split_settings.tools import include

LOCAL_SETTINGS = [
    'base.py',
]

include(*LOCAL_SETTINGS)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'local'
# CELERY_ALWAYS_EAGER = True
HOSTNAME = '127.0.0.1'

ALLOWED_HOSTS = ['*']
