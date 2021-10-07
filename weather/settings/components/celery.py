from weather.settings.components.django_environ import env
import types

CELERY_BROKER_URL = f"redis://{env('REDIS_HOST')}:{env('REDIS_PORT')}/0"
BROKER_TRANSPORT_OPTIONS = types.MappingProxyType({"visibility_timeout": 3600})
CELERY_IGNORE_RESULT = True
CELERY_STORE_ERRORS_EVEN_IF_IGNORED = False
CELERY_ACCEPT_CONTENT = ("json",)
CELERY_TASK_SERIALIZER = "json"
CELERYBEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"