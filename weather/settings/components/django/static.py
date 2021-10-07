import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0.4/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

FAVICON_CONFIG = {
    'shortcut icon': [16 ,32 ,48 ,128, 192],
    'touch-icon': [196],
    'icon': [196],
    'apple-touch-icon': [57, 72, 114, 144, 180],
    'apple-touch-icon-precomposed': [57, 72, 76, 114, 120, 144, 152,180],
}