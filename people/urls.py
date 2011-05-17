from django.conf.urls.defaults import patterns

urlpatterns = patterns( 'people.views',
    ( r'^import_select/(?P<event_id>\d+)$', 'import_select' ),
    ( r'^import_finish/(?P<event_id>\d+)/(?P<folder>[\w|\W]+)$', 'import_finish' ),
 )
