from django.conf.urls.defaults import *

urlpatterns = patterns( 'facebook_app.views',
    url( r'^$', 'events_list', name='facebook_events_list' ),
    url( r'^photos$', 'albums_list', name='facebook_albums_list' ),
    url( r'^photos/(?P<id>\d+)$', 'photos_list', name='facebook_photos_list' ),
)