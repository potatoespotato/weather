from django.conf import settings
from django.contrib.staticfiles.storage import ManifestFilesMixin, StaticFilesStorage
from django.core.files.storage import FileSystemStorage
from storages.backends.s3boto3 import S3Boto3Storage


class AWSMixin:
    def __init__(self, *args, **kwargs):
        if hasattr(settings, 'CDN_DOMAIN'):
            kwargs['custom_domain'] = settings.CDN_DOMAIN
        super().__init__(*args, **kwargs)


class S3MediaStorage(AWSMixin, S3Boto3Storage):
    location = 'media'
    file_overwrite = False


class S3StaticStorage(AWSMixin, ManifestFilesMixin, S3Boto3Storage):
    file_overwrite = True


class LocalMediaStorage(FileSystemStorage):
    pass


class LocalStaticStorage(StaticFilesStorage):
    pass
