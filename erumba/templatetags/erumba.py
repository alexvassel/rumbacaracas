from django import template
register = template.Library()

from yourphotos.models import Photo
from yourvideos.models import Video
from events.models import Event
from people.models import PhotoEvent
import itertools
import datetime
import dateutil.parser
from django.template.defaultfilters import date

@register.inclusion_tag( 'erumba/tags/your_photos.html' )
def last_yourphotos( number = 2 ):
    photos = Photo.objects.filter(status=1).order_by('-datetime_added')[:number]
    return dict(photos=photos)

@register.inclusion_tag( 'erumba/tags/your_videos.html' )
def last_yourvideos( number = 2 ):
    videos = Video.objects.filter(status=1).order_by('-datetime_added')[:number]
    return dict(videos=videos)

@register.inclusion_tag( 'erumba/tags/upcoming_events.html' )
def upcoming_events(from_date = datetime.date.today(), to_date = datetime.date.today() + datetime.timedelta(6)):

    from_date = datetime.datetime.combine(from_date, datetime.time())
    to_date   = datetime.datetime.combine(to_date, datetime.time())

    event_list = list(Event.objects.get_occuriences(start_date=from_date, end_date=to_date))
    sorted_events = sorted( event_list, key = lambda o: o[1], reverse=True)

    def sortList( list ):
        list.sort( key = lambda a:a[0].position, reverse = False )
        return list

    by_day = list([
       (dom, sortList( list(items) )) for dom, items in itertools.groupby( sorted_events, lambda o: o[1] )
    ])
    by_day.reverse()

    by_day = ([
        (dom, list([item[0] for item in items])) for dom, items in by_day
    ])

    return {
        'from_date': from_date,
        'to_date': to_date,
        'events_by_day': by_day
    }

@register.inclusion_tag( 'erumba/tags/latest_photos.html' )
def latests_photos():
    photos = PhotoEvent.objects.filter( status = 1 ).order_by( '-datetime_added', '-id' )[:3]
    return {'photos': photos}