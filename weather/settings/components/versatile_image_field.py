# VersatileImageField settings
VERSATILEIMAGEFIELD_SETTINGS = {
    'cache_length': 60 * 60 * 24 * 30 * 12,
    'cache_name': 'versatileimagefield_cache',
    'jpeg_resize_quality': 70,
    # TOOD: Write prewarm signals and set 'create_images_on_demand' to False
    'create_images_on_demand': True,
    'image_key_post_processor': None,
    'progressive_jpeg': False
}

# TODO: Write prewarm keysets
# VERSATILEIMAGEFIELD_RENDITION_KEY_SETS = {
#     'some_name': [
#         ('jumbotron_background', 'crop__1250x690'),
#         ('jumbotron_preview_image', 'crop__470x300'),
#         ('jumbotron_preview_image_2x', 'crop__940x600'),
#     ],
# }


UPLOAD_TO_PATHS = dict(
    # ModelName='upload_images/modelname/%Y/%m/%d/',
    )
