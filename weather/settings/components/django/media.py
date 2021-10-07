import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0.4/howto/static-files/

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
