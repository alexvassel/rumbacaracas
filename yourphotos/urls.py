from django.conf.urls.defaults import *

urlpatterns = patterns( 'yourphotos.views',
    ( r'^$', 'photos', {'category': 'latest'} ),
    ( r'^add$', 'add' ),
    ( r'^delete/(?P<id>\d+)$', 'delete' ),
    ( r'^(?P<category>(latest|sexy|rumbas|amigos|humor))$', 'photos' ),
    url( r'^(?P<id>\d+)$', 'detail' , name = "yourphoto_details" ),
 )
