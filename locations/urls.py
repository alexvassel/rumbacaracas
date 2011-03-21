from django.conf.urls.defaults import *

urlpatterns = patterns( 'locations.views',
    ( r'^$', 'category' ),
    ( r'^by-category$', 'category' ),
    ( r'^by-category/(?P<slug>[-w]+)$', 'category_detail' ),
    ( r'^by-area$', 'area' ),
    ( r'^by-area/(?P<slug>[-w]+)$', 'area_detail' ),
    ( r'^by-music$', 'music' ),
    ( r'^by-music/(?P<slug>[-w]+)$', 'music_detail' ),
    ( r'^by-food$', 'food' ),
    ( r'^by-food/(?P<slug>[-w]+)$', 'food_detail' ),
    ( r'^(?P<slug>[-\w]+)/$', 'detail' ),
 )
