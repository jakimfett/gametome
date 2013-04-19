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

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'gametome.wsgi_dev.application'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = normpath(join(PROJECT_ROOT, 'static_root'))

INSTALLED_APPS += (
    # Any dev-only apps to include
    'devserver',
)

# Django Cacheing
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
'''CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
'''
