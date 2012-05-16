from django.conf.urls import patterns, url

from views import *


urlpatterns = patterns('',
    url(r'^$', DashView.as_view(), name='medoco_dash'),
    url(r'^type/new$', TypeView.as_view(), name='medoco_type_new'),
    url(r'^type/list$', TypeListView.as_view(), name='medoco_type_list'),
    url(r'^type/(?P<type_id>\w+)$', TypeView.as_view(), name='medoco_type'),
    url(r'^type/delete$', TypeDeleteView.as_view(), name='medoco_type_delete'),
)
