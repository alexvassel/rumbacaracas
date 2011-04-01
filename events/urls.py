from django.conf.urls.defaults import *

urlpatterns = patterns( 'events.views',
    ( r'^$', 'category' ),
    ( r'^by-category/$', 'category', {'period': 'day'} ),
    ( r'^by-category/today$', 'category', {'period': 'day'} ),
    ( r'^by-category/tomorrow$', 'category', {'period': 'day'} ),
    ( r'^by-category/week$', 'category' ),
    ( r'^by-category/month$', 'category' ),

    ( r'^by-category/day/(?P<year>\d{4})/(?P<month>0?[1-9]|1[012])/(?P<day>[0-3]?\d)$', 'category' ),
    ( r'^by-category/week/(?P<year>\d{4})/(?P<week>\d+)$', 'category' ),
    ( r'^by-category/month/(?P<year>\d{4})/(?P<month>0?[1-9]|1[012])$', 'category' ),

    ( r'^by-area$', 'area', {'period': 'day'} ),
    ( r'^by-area$/today$', 'area', {'period': 'day'} ),
    ( r'^by-area$/tomorrow$', 'area', {'period': 'day'} ),
    ( r'^by-area$/week$', 'area', {'period': 'week'} ),
    ( r'^by-area$/month$', 'area', {'period': 'month'} ),

    ( r'^by-music$', 'music', {'period': 'day'} ),
    ( r'^by-music$/today$', 'music', {'period': 'day'} ),
    ( r'^by-music$/tomorrow$', 'music', {'period': 'day'} ),
    ( r'^by-music$/week$', 'music', {'period': 'week'} ),
    ( r'^by-music$/month$', 'music', {'period': 'month'} ),

    ( r'^by-location$', 'location' , {'period': 'day'} ),
    ( r'^by-location$/today$', 'location', {'period': 'day'} ),
    ( r'^by-location$/tomorrow$', 'location', {'period': 'day'} ),
    ( r'^by-location$/week$', 'location' , {'period': 'week'} ),
    ( r'^by-location$/month$', 'location', {'period': 'month'} ),

    ( r'^calendar$', 'calendar_view' ),
    ( r'^calendar/(?P<year>\d{4})/(?P<month>0?[1-9]|1[012])/$', 'calendar_view' ),
    ( r'^(?P<slug>[-\w]+)/$', 'detail' ),
 )
