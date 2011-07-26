from django import template
register = template.Library()

from events.models import Event 
from yourphotos.models import Photo
from yourvideos.models import Video
from locations.models import Location
from zinnia.models import Entry
from people.models import PhotoEvent
import calendar
from datetime import datetime, timedelta, time
import itertools
from django.template.defaultfilters import date
from decorators import cache

@cache(600)
@register.inclusion_tag( 'widgets/magazine.html' )
def magazine_block( ):
    return dict()

@register.inclusion_tag( 'widgets/subscribe.html' )
def subscribe_block( ):
    return dict()

@cache(600)
@register.inclusion_tag( 'widgets/yourphotos.html' )
def yourphotos_block( ):
    photos = Photo.objects.filter(status=1).order_by('-datetime_added')[:2]
    return dict(photos=photos)

@cache(600)
@register.inclusion_tag( 'widgets/people.html' )
def people_block( ):
    events = PhotoEvent.objects.filter(status=1).order_by('-datetime_added')[:4]
    return dict(events=events)

@cache(600)
@register.inclusion_tag( 'widgets/people_list.html' )
def people_list( ):
    events = PhotoEvent.objects.filter(status=1).order_by('-datetime_added')[:6]
    return dict(events=events)


@cache(600)
@register.inclusion_tag( 'widgets/latest_news.html' )
def news_list( ):
    news = Entry.published.all()[:10]
    return dict(news=news)


@cache(600)
@register.inclusion_tag( 'widgets/locations.html' )
def location_list( ):
    locations = Location.objects.filter(status=1).order_by('?')[:20]
    return dict(locations=locations)

@cache(600)
@register.inclusion_tag( 'widgets/locations_block.html' )
def location_block( ):
    locations = Location.objects.filter(status=1).order_by('?')[:2]
    return dict(locations=locations)

@cache(600)
@register.inclusion_tag( 'widgets/art_culture.html' )
def art_culture_block( ):
    today = datetime.today()
    #TODO wrong check if upcoming
    events = Event.objects.filter(status=1, category=4, to_date__gte = today)[:2]
    return dict(events=events)

@cache(600)
@register.inclusion_tag('widgets/today_events_list.html')
def get_event_list(number=5):
    """Return the most recent entries"""
    return {'entries': Entry.published.all()[:number]}


@cache(600)
@register.inclusion_tag( 'widgets/videos.html' )
def yourvideos_block( exclude = None ):
    videos = Video.objects.filter(status=1).order_by('-datetime_added')

    if exclude:
        videos = videos.exclude(pk=exclude.id)

    return dict(videos=videos[:4])

@cache(600)
@register.inclusion_tag('widgets/upcoming_events_list.html')
def upcoming_events_list(count = 6 ):
    today = datetime.today()
    #TODO wrong check if upcoming
    event_list = Event.objects.filter(status=1,to_date__gte = today)[:count]
    return dict(events = event_list)

@cache(600)
@register.inclusion_tag('widgets/upcoming_events_block.html')
def upcoming_events_block(count = 4 ):
    today = datetime.today()
    #TODO wrong check if upcoming
    event_list = Event.objects.filter(status=1,to_date__gte = today)[:count]
    return dict(events = event_list)



@cache(600)
@register.inclusion_tag('widgets/events_today_block.html')
def events_today_block( ):

    today = datetime.today()
    zdat_day = datetime.today() + timedelta(2)

    dtstart = datetime( today.year, today.month, today.day )
    dtend = datetime( zdat_day.year, zdat_day.month, zdat_day.day )

    event_list = Event.objects.get_occuriences(start_date=dtstart, end_date=dtend)
    sorted_events = sorted( event_list, key = lambda o: date(o[1], "l"))

    def sortList( list ):
        list.sort( key = lambda a:a[0].position, reverse = False )
        return list

    by_day = list([
        ( dom, sortList( list( items ) ) ) for dom, items in itertools.groupby( sorted_events, lambda o: date(o[1], "l") )
    ])
    by_day.reverse()

    return dict(days = by_day)



def get_last_day_of_month(year, month):
    if (month == 12):
        year += 1
        month = 1
    else:
        month += 1
    return date(year, month, 1) - timedelta(1)

@cache(600)
@register.inclusion_tag('widgets/calendar.html')
def month_cal(year=None, month=None):

    today = datetime.today()

    if year is None:
        year = today.year
    if month is None:
        month = today.month

    calendar.setfirstweekday( 6 )
    dtstart = datetime( year, month, 1 )
    last_day = calendar.monthrange( year, month )[1]
    dtend = datetime( year, month, last_day )

    event_list = Event.objects.get_occuriences(start_date=dtstart, end_date=dtend)
    events_dates = [dt for event, dt in event_list]

    first_day_of_month = dtstart.date()
    last_day_of_month = dtend.date()
    
    first_day_of_calendar = first_day_of_month - timedelta(first_day_of_month.weekday())
    last_day_of_calendar = last_day_of_month + timedelta(7 - last_day_of_month.weekday())




    month_cal = []
    week = []
    week_headers = []

    i = 0
    day = first_day_of_calendar
    while day <= last_day_of_calendar:
        if i < 7:
            week_headers.append(day)
        cal_day = {}
        cal_day['day'] = day
        cal_day['event'] = False
        cal_day['in_month'] = False

        if day in events_dates:
            cal_day['event'] = True

        if day.month == month:
            cal_day['in_month'] = True

        week.append(cal_day)
        if day.weekday() == 6:
            month_cal.append(week)
            week = []
        i += 1
        day += timedelta(1)

    return {'calendar': month_cal, 'headers': week_headers, 'first_day_of_month': first_day_of_month }

