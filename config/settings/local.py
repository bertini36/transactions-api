from .base import *

# APP CONFIGURATION
# ******************************************************************************

# TEMPLATES
# ------------------------------------------------------------------------------
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

# ALLOWED HOSTS
# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
# ------------------------------------------------------------------------------
ALLOWED_HOSTS = ['*']

# THIRD PARTY APPLICATIONS
# ******************************************************************************

# DJANGO DEBUG TOOLBAR
# https://github.com/jazzband/django-debug-toolbar
# ------------------------------------------------------------------------------
INSTALLED_APPS += ('debug_toolbar',)
MIDDLEWARE += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
INTERNAL_IPS = [
    '127.0.0.1',
]
DEBUG_TOOLBAR_CONFIG = {'SHOW_TOOLBAR_CALLBACK': lambda _: True}

# Django-extensions
# https://github.com/django-extensions/django-extensions
# ------------------------------------------------------------------------------
INSTALLED_APPS += ('django_extensions',)
