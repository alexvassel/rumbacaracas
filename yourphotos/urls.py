from django.conf.urls.defaults import *

urlpatterns = patterns( 'yourphotos.views',
    ( r'^$', 'photos', {'category': 'latest'} ),
    ( r'^add$', 'add' ),
    ( r'^(?P<category>(latest|sexy|rumbas|amigos|humor))$', 'photos' ),
    ( r'^(?P<id>\d+)$', 'detail' ),
 )
