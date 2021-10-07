CKEDITOR_UPLOAD_PATH = "uploads/html_field/"
# CKEDITOR_FILENAME_GENERATOR = 'apps.main.utils.path_and_rename'
CKEDITOR_UPLOAD_SLUGIFY_FILENAME = True
CKEDITOR_RESTRICT_BY_DATE = True
AWS_QUERYSTRING_AUTH = False
CKEDITOR_BROWSE_SHOW_DIRS = False
CKEDITOR_CONFIGS = {
    'default': {
        'width': '100%',
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Styles', 'Format', 'Font', 'FontSize'],
            ['TextColor', 'BGColor'],
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter',
             'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink'],
            ['RemoveFormat', 'Source', 'Image'],
        ]
    },
    'simple': {
        'width': '100%',
        'tabSpaces': 4,
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
        ]
    }
}
