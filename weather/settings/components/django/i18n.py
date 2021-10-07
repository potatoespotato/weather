# Internationalization
# https://docs.djangoproject.com/en/3.0.4/topics/i18n/
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True


USE_I18N = True

USE_L10N = True

LOCALE_PATHS = (BASE_DIR + '/apps/locale', )