# Urls for app 'gtdb'
from django.conf.urls import patterns, include, url

urlpatterns = patterns('gtdb.views',
    # Examples:
    url(r'^$', 'index', name='index'),
    url(r'^games/$', 'games', name='games'),
)
