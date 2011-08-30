from django.conf.urls.defaults import *

urlpatterns = patterns( 'locations.views',
    url( r'^$', 'category', name='location_main' ),
    url( r'^publica$', 'add', name='location_add' ),
    url( r'^por-tipo$', 'category', name='location_by_category' ),
    url( r'^por-zona$', 'area', name='location_by_area' ),
    url( r'^por-musica$', 'music', name='location_by_music' ),
    url( r'^por-comida$', 'food', name='location_by_food' ),
    url( r'^tipo/(?P<group>\w+)$', "category_details" , name = "location_category" ),
    url( r'^(?P<slug>[-\w]+)/$', "detail", name = "location_details" ),
 )
