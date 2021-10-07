from weather.settings.components.django_environ import env

# Django-cacheops settings
# https://github.com/Suor/django-cacheops
CACHE_MIDDLEWARE_SECONDS = 60

CACHEOPS_REDIS = f"redis://{env('REDIS_HOST')}:{env('REDIS_PORT')}/{env('REDIS_DB')}"

CACHEOPS = {

}
