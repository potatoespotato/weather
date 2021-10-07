from weather.settings.components.django_environ import env

# Django cache settings
# https://docs.djangoproject.com/en/3.0.4/topics/cache/

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': f"redis://{env('REDIS_HOST')}:{env('REDIS_PORT')}/{env('REDIS_DB')}",
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient'
        },
        'KEY_PREFIX': 'trs:cache',
        'TIMEOUT': 600,
        'MAX_ENTRIES': 5000,
    },
}
