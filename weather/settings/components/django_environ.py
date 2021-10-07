import environ

# Django environ settings
# https://django-environ.readthedocs.io/en/latest/

env = environ.Env(
    DEBUG=(bool, False),
    SECRET_KEY=(str, 'weatherSecretKey'),
    ALLOWED_HOSTS=(str, '*'),

    REDIS_HOST=(str, 'redis'),
    REDIS_PORT=(int, 6379),
    REDIS_DB=(int, 1),

    API_KEY=(str, '')

)
