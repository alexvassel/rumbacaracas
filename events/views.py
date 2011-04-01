from django.shortcuts import get_object_or_404
from events.models import EventCategory, Event, WeekDay
from locations.models import LocationArea, Location, LocationMusic
from django.utils.translation import ugettext as _
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from decorators import render_to
import calendar
from datetime import datetime, timedelta, time

months = {
        1 : "January",
        2 : "February",
        3 : "March",
        4 : "April",
        5 : "May",
        6 : "June",
        7 : "July",
        8 : "August",
        9 : "September",
        10 : "October",
        11 : "November",
        12 : "December",
}


def _process( request, group ):
    group_fields = group.objects.select_related().all()
    groups = []
    counter = 0
    for group in group_fields:
        events = group.event_set.all()
        if events:
            groups.append( ( group.title , events ) )


    current_year = datetime.today().year
    years = range( current_year - 5, current_year + 5 )

    slider_events = Event.objects.order_by( '?' )[:5]
    all_events = Event.objects.all().order_by( 'title' )
    return {'all_events': all_events, 'groups': groups, 'slider_events': slider_events, 'years': years, 'months': months}

calendar.setfirstweekday( 6 )
#MO, TU, WE, TH, FR, SA, SU
@render_to( 'events/calendar.html' )
def calendar_view( 
    request
    , year = 0, month = 0
 ):
    #year, month = int( year ), int( month )

    all_events = Event.objects.all().order_by( 'title' )
    request.breadcrumbs( _( 'Events' ) , '/events' )
    request.breadcrumbs( _( 'Calendar' ) , request.path_info )

    if year == 0:
        year = datetime.today().year
    else:
        year = int( year )
    if month == 0:
        month = datetime.today().month
    else:
        month = int( month )

    cal = calendar.monthcalendar( year, month )
    dtstart = datetime( year, month, 1 )
    last_day = max( cal[-1] )


    # TODO Whether to include those occurrences that started in the previous
    # month but end in this month?
    calendars = Event.objects.get_month( year = year, month = month )

    current_year = datetime.today().year
    years = range( current_year - 5, current_year + 5 )

    slider_events = Event.objects.order_by( '?' )[:5]

    return dict( 
        today = datetime.now(),
        calendar = calendars,
        this_month = dtstart,
        next_month = dtstart + timedelta( days = +last_day ),
        last_month = dtstart + timedelta( days = -1 ),
        years = years,
        year = year,
        months = months,
        month = month,
        all_events = all_events,
        slider_events = slider_events,
        active_tab = 'calendar'
    )





@render_to( 'events/grouping.html' )
def category( request , period = 'day', date_parameter = 0 ):
    request.breadcrumbs( _( 'Events' ) , '/events' )
    request.breadcrumbs( _( 'By Category' ) , request.path_info )
    dict = _process( request, EventCategory )
    dict['active_tab'] = 'category'
    return dict


@render_to( 'events/grouping.html' )
def area( request ):
    request.breadcrumbs( _( 'Events' ) , '/events' )
    request.breadcrumbs( _( 'By Area' ) , request.path_info )
    dict = _process( request, LocationArea )
    dict['active_tab'] = 'area'
    return dict


@render_to( 'events/grouping.html' )
def location( request ):
    request.breadcrumbs( _( 'Events' ) , '/events' )
    request.breadcrumbs( _( 'By Location' ) , request.path_info )
    dict = _process( request, Location )
    dict['active_tab'] = 'location'
    return dict


@render_to( 'events/grouping.html' )
def music( request ):
    request.breadcrumbs( _( 'Events' ) , '/events' )
    request.breadcrumbs( _( 'By Music' ) , request.path_info )
    dict = _process( request, LocationMusic )
    dict['active_tab'] = 'music'
    return dict

@render_to( 'events/details.html' )
def detail ( request, slug ):
    event = get_object_or_404( Event, slug = slug )
    request.breadcrumbs( _( 'Events' ) , '/events' )
    request.breadcrumbs( event.title , request.path_info )
    dict = _process( request, EventCategory )
    dict['event'] = event
    dict['active_tab'] = 'category'
    return dict
