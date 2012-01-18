from django.conf.urls.defaults import *

urlpatterns = patterns( 'cities.views',
    url( r'^$', 'index', name='city_index' ),
    #url( r'^publica$', 'add', name='location_add' ),
    #url( r'^por-tipo$', 'category', name='location_by_category' ),
    #url( r'^por-tipo$', 'category', name='location_by_category' ),
    #url( r'^por-zona$', 'area', name='location_by_area' ),
    #url( r'^por-musica$', 'music', name='location_by_music' ),
    #url( r'^por-comida$', 'food', name='location_by_food' ),
    url( r'^(?P<city>[-\w]+)$', 'city_index', name = "cities_category" ),
    #url( r'^(?P<slug>[-\w]+)/$', "detail", name = "location_details" ),
 )
