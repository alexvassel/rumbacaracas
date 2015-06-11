from django.conf.urls.defaults import *

urlpatterns = patterns( 'people.views',
    url( r'^$', 'index', name='people_main' ),
    url( r'^request', 'request', name='people_request' ),
    url( r'^tipo/(?P<group>\w+)$', "category" , name = "people_category" ),
    url( r'^make_main/(?P<event_id>\d+)/(?P<photo_id>\d+)$', "make_main", name="people_make_main" ),
    url( r'^import_select/(?P<event_id>\d+)$', 'import_select', name='people_admin_select' ),
    url( r'^import_finish/(?P<event_id>\d+)/(?P<folder>[\w|\W]+)$', 'import_finish', name='people_admin_finish' ),
    url( r'^main_slide/(?P<event_id>\d+)$', 'main_slide', name='people_main_slide' ),
    url( r'^(?P<slug>[\w|\W]+)/(?P<photo_id>\d+)$', "slider" , name = "people_slider" ),
    url( r'^(?P<slug>[\w|\W]+)$', "details" , name = "people_details" ),
 )
