from django.conf.urls import patterns, include, url

from ..app import urls as app_urls


urlpatterns = patterns('',
    url(r'^', include(app_urls)),
)
