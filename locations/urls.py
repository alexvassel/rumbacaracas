from django.conf.urls.defaults import *

urlpatterns = patterns( 'locations.views',
    ( r'^$', 'category' ),
    ( r'^add$', 'add' ),
    ( r'^by-category$', 'category' ),
    ( r'^by-area$', 'area' ),
    ( r'^by-music$', 'music' ),
    ( r'^by-food$', 'food' ),
    ( r'^(?P<slug>[-\w]+)/$', 'detail' ),
 )
