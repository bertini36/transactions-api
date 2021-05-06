from .base import *

# SITE CONFIGURATION
# https://docs.djangoproject.com/en/1.6/ref/settings/#allowed-hosts
# ------------------------------------------------------------------------------
ALLOWED_HOSTS = ('https://www.abacum.io/',)

# TEMPLATE CONFIGURATION
# https://docs.djangoproject.com/en/dev/ref/templates/api/#django.template.loaders.cached.Loader
# ------------------------------------------------------------------------------
TEMPLATES[0]['OPTIONS']['loaders'] = [
    (
        'django.template.loaders.cached.Loader',
        [
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        ],
    ),
]
