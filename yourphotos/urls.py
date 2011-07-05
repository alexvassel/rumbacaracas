from django.conf.urls.defaults import *

urlpatterns = patterns( 'yourphotos.views',
    ( r'^$', 'photos', {'category': 'latest'} ),
    ( r'^add$', 'add' ),
    ( r'^delete/(?P<id>\d+)$', 'delete' ),
    ( r'^(?P<category>(latest|sexy|rumbas|amigos|humor))$', 'photos' ),
    ( r'^main_slide/(?P<photo_id>\d+)$', 'main_slide' ),
    url( r'^(?P<id>\d+)$', 'detail' , name = "yourphoto_details" ),
 )
