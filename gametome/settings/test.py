# Django Dev settings for {{ project_name }} project.

from os.path import normpath, join
from .common import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG
# This makes runserver send exceptions to the console
# DEBUG_PROPAGATE_EXCEPTIONS = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', 
        'NAME': normpath(join(PROJECT_ROOT, 'default.db')),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

INSTALLED_APPS += (
    # Production-only packages to include
)

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'gametome.wsgi_test.application'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = '/opt/gametome/static/'

# Cache parsed templates
TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', TEMPLATE_LOADERS),
)

# Django Cacheing
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}




