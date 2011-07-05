from django.conf.urls.defaults import *

urlpatterns = patterns( 'people.views',
    ( r'^$', 'index' ),
    url( r'^category/(?P<group>\w+)$', "category" , name = "people_category" ),
    url( r'^slider/(?P<photo_id>\d+)$', "slider" , name = "people_slider" ),
    ( r'^make_main/(?P<event_id>\d+)/(?P<photo_id>\d+)$', 'make_main' ),
    ( r'^import_select/(?P<event_id>\d+)$', 'import_select' ),
    ( r'^import_finish/(?P<event_id>\d+)/(?P<folder>[\w|\W]+)$', 'import_finish' ),
    ( r'^main_slide/(?P<event_id>\d+)$', 'main_slide' ),
    url( r'^(?P<slug>[\w|\W]+)$', "details" , name = "people_details" ),
 )
