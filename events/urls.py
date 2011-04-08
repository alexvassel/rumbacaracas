from django.conf.urls.defaults import patterns

urlpatterns = patterns( 'events.views',
    ( r'^$', 'category', {'period': 'day'} ),

    ( r'^by-category/$', 'category', {'period': 'day'} ),
    ( r'^by-category/day$', 'category', {'period': 'day'} ),
    ( r'^by-category/tomorrow$', 'category', {'period': 'tomorrow'} ),
    ( r'^by-category/day/(?P<year>\d{4})/(?P<month>0?[1-9]|1[012])/(?P<day>[0-3]?\d)$', 'category', {'period': 'day'} ),
    ( r'^by-category/week$', 'category' , {'period': 'week'} ),
    ( r'^by-category/week/(?P<year>\d{4})/(?P<month>0?[1-9]|1[012])/(?P<day>[0-3]?\d)$', 'category' , {'period': 'week'} ),
    ( r'^by-category/month$', 'category' , {'period': 'month'} ),
    ( r'^by-category/month/(?P<year>\d{4})/(?P<month>0?[1-9]|1[012])$', 'category', {'period': 'month'} ),

    ( r'^by-area$', 'area', {'period': 'day'} ),
    ( r'^by-area/day$', 'area', {'period': 'day'} ),
    ( r'^by-area/tomorrow$', 'area', {'period': 'tomorrow'} ),
    ( r'^by-area/day/(?P<year>\d{4})/(?P<month>0?[1-9]|1[012])/(?P<day>[0-3]?\d)$', 'area', {'period': 'day'} ),
    ( r'^by-area/week$', 'area' , {'period': 'week'} ),
    ( r'^by-area/week/(?P<year>\d{4})/(?P<month>0?[1-9]|1[012])/(?P<day>[0-3]?\d)$', 'area' , {'period': 'week'} ),
    ( r'^by-area/month$', 'area' , {'period': 'month'} ),
    ( r'^by-area/month/(?P<year>\d{4})/(?P<month>0?[1-9]|1[012])$', 'area', {'period': 'month'} ),

    ( r'^by-music$', 'music', {'period': 'day'} ),
    ( r'^by-music/day$', 'music', {'period': 'day'} ),
    ( r'^by-music/tomorrow$', 'music', {'period': 'tomorrow'} ),
    ( r'^by-music/day/(?P<year>\d{4})/(?P<month>0?[1-9]|1[012])/(?P<day>[0-3]?\d)$', 'music', {'period': 'day'} ),
    ( r'^by-music/week$', 'music' , {'period': 'week'} ),
    ( r'^by-music/week/(?P<year>\d{4})/(?P<month>0?[1-9]|1[012])/(?P<day>[0-3]?\d)$', 'music' , {'period': 'week'} ),
    ( r'^by-music/month$', 'music' , {'period': 'month'} ),
    ( r'^by-music/month/(?P<year>\d{4})/(?P<month>0?[1-9]|1[012])$', 'music', {'period': 'month'} ),

    ( r'^by-location$', 'location' , {'period': 'day'} ),
    ( r'^by-location/day$', 'location', {'period': 'day'} ),
    ( r'^by-location/tomorrow$', 'location', {'period': 'tomorrow'} ),
    ( r'^by-location/day/(?P<year>\d{4})/(?P<month>0?[1-9]|1[012])/(?P<day>[0-3]?\d)$', 'location', {'period': 'day'} ),
    ( r'^by-location/week$', 'location' , {'period': 'week'} ),
    ( r'^by-location/week/(?P<year>\d{4})/(?P<month>0?[1-9]|1[012])/(?P<day>[0-3]?\d)$', 'location' , {'period': 'week'} ),
    ( r'^by-location/month$', 'location' , {'period': 'month'} ),
    ( r'^by-location/month/(?P<year>\d{4})/(?P<month>0?[1-9]|1[012])$', 'location', {'period': 'month'} ),

    ( r'^calendar$', 'calendar_view' , {'period': 'month'} ),
    ( r'^calendar/(?P<year>\d{4})/(?P<month>0?[1-9]|1[012])/$', 'calendar_view', {'period': 'month'} ),

    ( r'^(?P<slug>[-\w]+)/$', 'detail' , {'period': 'month'} ),
    ( r'^(?P<slug>[-\w]+)/by-category$', 'detail' , {'period': 'month'} ),
 )
