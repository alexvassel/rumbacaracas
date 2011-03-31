from django.conf.urls.defaults import *

urlpatterns = patterns( 'events.views',
    ( r'^$', 'category' ),
    ( r'^by-category/$', 'category' ),
    ( r'^by-category/day/(\d{4})/(0?[1-9]|1[012])/([0-3]?\d)$', 'category' ),
    ( r'^by-category/week/(\d{4})/(\d+)$', 'category' ),
    ( r'^by-category/month/(\d{4})/(0?[1-9]|1[012])$', 'category' ),

    ( r'^by-area$', 'area' ),
    ( r'^by-music$', 'music' ),
    ( r'^by-location$', 'location' ),
    ( r'^calendar$', 'calendar_view' ),
    #( r'^(?:calendar/)?$', 'month' ),
    ( r'^calendar/(\d{4})/(0?[1-9]|1[012])/$', 'calendar_view' ),
    ( r'^(?P<slug>[-\w]+)/$', 'detail' ),
 )
