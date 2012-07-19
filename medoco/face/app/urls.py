from django.conf.urls import patterns, url

from views import *


urlpatterns = patterns('',
    url(r'^$', DashView.as_view(), name='medoco_dash'),
    url(r'^docspec/new$', DocSpecView.as_view(), name='medoco_doc_spec_new'),
    url(r'^docspec/list$', DocSpecListView.as_view(),
        name='medoco_doc_spec_list'),
    url(r'^docspec/(?P<doc_spec_id>\w+)$', DocSpecView.as_view(),
        name='medoco_doc_spec'),
    url(r'^docspec/delete$', DocSpecDeleteView.as_view(),
        name='medoco_doc_spec_delete'),
)
