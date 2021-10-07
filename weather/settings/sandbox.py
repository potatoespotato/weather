from split_settings.tools import include

SANDBOX_SETTINGS = [
    'base.py',
]
include(*SANDBOX_SETTINGS)
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'sandbox'

HOSTNAME = ''

ALLOWED_HOSTS = ['*']

