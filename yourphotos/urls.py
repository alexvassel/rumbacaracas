from django.conf.urls.defaults import *

urlpatterns = patterns( 'yourphotos.views',
    ( r'^$', 'photos', {'category': 'sexy'} ),
    ( r'^add$', 'add' ),
    ( r'^(?P<category>(sexy|rumbas|amigos|humor))$', 'photos' ),
    ( r'^(?P<id>\d+)$', 'detail' ),
 )
