from django.conf.urls.defaults import patterns

urlpatterns = patterns( 'peoples.views',
    ( r'^import_select/(?P<event_id>\d+)$', 'import_select' ),
    ( r'^import_finish/(?P<event_id>\d+)/(?P<folder>\w+)$', 'import_finish' ),
 )
