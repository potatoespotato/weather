from weather.settings.components.django_environ import env
AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')

AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=31536000'}
AWS_PRELOAD_METADATA = True
S3_USE_SIGV4 = True
AWS_S3_REGION_NAME = 'eu-central-1'
AWS_LOCATION = 'static'

DEFAULT_FILE_STORAGE = 'weather.storages.S3MediaStorage'
STATICFILES_STORAGE = 'weather.storages.S3StaticStorage'

AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_QUERYSTRING_AUTH = False
AWS_S3_FILE_OVERWRITE = True
AWS_DEFAULT_ACL = 'public-read'

MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/media/"
STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/static/"
AWS_HEADERS = {
    'Cache-Control': f'public, max-age=31536000',
}
# End S3 Section

GZIP_CONTENT_TYPES = [
    'application/atom+xml',
    'application/javascript',
    'application/json',
    'application/ld+json',
    'application/manifest+json',
    'application/rss+xml',
    'application/geo+json',
    'application/vnd.ms-fontobject',
    'application/x-web-app-manifest+json',
    'application/xhtml+xml',
    'application/xml',
    'application/rdf+xml',
    'font/otf',
    'application/wasm',
    'image/bmp',
    'image/svg+xml',
    'text/cache-manifest',
    'text/css',
    'text/javascript',
    'text/plain',
    'text/markdown',
    'text/vcard',
    'text/calendar',
    'text/vnd.rim.location.xloc',
    'text/vtt',
    'text/x-component',
    'text/x-cross-domain-policy;',
]
AWS_IS_GZIPPED = True
