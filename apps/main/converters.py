from django.urls.converters import SlugConverter


class SlugOrNotConverter(SlugConverter):
    regex = '[-a-zA-Z0-9_]*'
