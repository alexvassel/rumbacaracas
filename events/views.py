from django.shortcuts import get_object_or_404
from events.models import EventCategory, Event, WeekDay
from locations.models import LocationArea, Location, LocationMusic
from django.utils.translation import ugettext as _
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from decorators import render_to
import calendar
from datetime import datetime, timedelta, time
import itertools

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

calendar.setfirstweekday( 6 )
#MO, TU, WE, TH, FR, SA, SU

def _process( request, group_lambda, period ):

    from_date, to_date = _process_period( period )

    events = Event.objects.get_occuriences( start_date = from_date, end_date = to_date )

    #group_lambda = lambda o: o[0].category
    sorted_events = sorted( events, key = group_lambda )

    by_group = dict( [
        ( group, list( items ) ) for group, items in itertools.groupby( sorted_events, group_lambda )
    ] )

    current_year = datetime.today().year
    years = range( current_year - 3, current_year + 3 )

    slider_events = Event.objects.order_by( '?' )[:5]
    all_events = Event.objects.all().order_by( 'title' )
    return {'all_events': all_events, 'groups': by_group, 'slider_events': slider_events, 'years': years, 'months': months}


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
    years = range( current_year - 3, current_year + 3 )

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



def _process_period( period ):
    if period == "day":
        from_date = datetime.today()
        to_date = datetime.today()
    elif period == "week":
        from_date = datetime.today()
        # Adjust the start datetime to Monday or Sunday of the current week
        sub_days = from_date.isoweekday() - 1
        if sub_days > 0:
            from_date = from_date - datetime.timedelta( days = sub_days )
        to_date = from_date + datetime.timedelta( days = 7 )
    elif period == "month":
        year = datetime.today().year
        month = datetime.today().month
        from_date = datetime( year, month, 1 )
        last_day = calendar.monthrange( year, month )[1]
        to_date = datetime( year, month, last_day )
    return ( from_date, to_date )

@render_to( 'events/grouping.html' )
def category( request , period = 'month', date_parameter = 0 ):
    request.breadcrumbs( _( 'Events' ) , '/events' )
    request.breadcrumbs( _( 'By Category' ) , request.path_info )
    dict = _process( request, lambda o: o[0].category, period )
    dict['active_tab'] = 'category'
    return dict


@render_to( 'events/grouping.html' )
def area( request , period = 'month' ):
    request.breadcrumbs( _( 'Events' ) , '/events' )
    request.breadcrumbs( _( 'By Area' ) , request.path_info )
    dict = _process( request, lambda o: o[0].area, period )
    dict['active_tab'] = 'area'
    return dict


@render_to( 'events/grouping.html' )
def location( request , period = 'month' ):
    request.breadcrumbs( _( 'Events' ) , '/events' )
    request.breadcrumbs( _( 'By Location' ) , request.path_info )
    dict = _process( request, lambda o: o[0].location, period )
    dict['active_tab'] = 'location'
    return dict


@render_to( 'events/grouping.html' )
def music( request, period = 'month' ):
    request.breadcrumbs( _( 'Events' ) , '/events' )
    request.breadcrumbs( _( 'By Music' ) , request.path_info )
    dict = _process( request, lambda o: o[0].music, period )
    dict['active_tab'] = 'music'
    return dict

@render_to( 'events/details.html' )
def detail ( request, slug ):
    event = get_object_or_404( Event, slug = slug )
    request.breadcrumbs( _( 'Events' ) , '/events' )
    request.breadcrumbs( event.title , request.path_info )
    dict = _process( request, lambda o: o[0].category, period )
    dict['event'] = event
    dict['active_tab'] = 'category'
    return dict
