from django.shortcuts import get_object_or_404
from events.models import EventCategory, Event, WeekDay
from locations.models import LocationArea, Location, LocationMusic
from django.utils.translation import ugettext as _
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from decorators import render_to
import calendar
from datetime import datetime, timedelta, time
import itertools
from django.template.defaultfilters import date
from dateutil.relativedelta import relativedelta

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

def f7( seq ):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if x not in seen and not seen_add( x )]

def _process( request, group_lambda, period , year = False, month = False, day = False ):

    from_date, to_date, repr, prev_date, next_date = _process_period( period, year, month, day )

    events = Event.objects.get_occuriences( start_date = from_date, end_date = to_date )

    tmp_events = list()
    tmp_dates = dict()
    tmp_closest_dates = dict()
    today = datetime.today()

    #Check if we show needed occurences
    for event, dt in events:
        if event not in tmp_events:
            tmp_events.append( event )
            tmp_dates[event.pk] = list()
        tmp_dates[event.pk].append( dt )

    min_period = False
    for pk, dts in tmp_dates.items():
        for dt in dts:
            if dt >= today.date():
                if not min_period or ( min_period and ( dt - today.date() ) < min_period ):
                    min_period = dt - today.date()
                    tmp_closest_dates[pk] = dt

        if ( pk not in tmp_closest_dates ):
            tmp_closest_dates[pk] = min( dts )


    sorted_events = sorted( tmp_events , key = group_lambda )

    by_group = dict( [
        ( group, list( items ) ) for group, items in itertools.groupby( sorted_events, group_lambda )
    ] )

    current_year = datetime.today().year
    years = range( current_year - 3, current_year + 3 )

    # SELECT ONLY UPCOMING!!!
    slider_events = Event.objects.filter( to_date__gte = datetime.today() ).order_by( '?' )[:5]


    all_locations = Location.objects.all()
    all_events = Event.objects.all().order_by( 'title' )

    #Seems like wrong
    year = from_date.year
    month = from_date.month
    day = from_date.day

    if period != "month":
        filter_date = '/' + str( year ) + '/' + str( month ) + '/' + str( day )
    else:
        filter_date = '/' + str( year ) + '/' + str( month )
    return {'filter_date': filter_date, 'all_locations': all_locations, 'all_events': all_events, 'groups': by_group, 'slider_events': slider_events, 'years': years, 'months': months, 'repr': repr, 'year': year, 'month': month, 'period': period, 'prev_date': prev_date, 'next_date': next_date, 'closest_dates': tmp_closest_dates}


@render_to( 'events/calendar.html' )
def calendar_view( 
    request
    , year = 0, month = 0, period = "month"
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

    slider_events = Event.objects.filter( to_date__gte = datetime.today() ).order_by( '?' )[:5]
    all_locations = Location.objects.all()

    return dict( 
        today = datetime.now(),
        calendar = calendars,
        this_month = dtstart,
        repr = date( dtstart, 'F, Y' ),
        next_date = dtstart + timedelta( days = +last_day ),
        prev_date = dtstart + timedelta( days = -1 ),
        filter_date = 'month/' + str( year ) + '/' + str( month ),
        years = years,
        year = year,
        months = months,
        month = month,
        all_events = all_events,
        all_locations = all_locations,
        slider_events = slider_events,
        active_tab = 'calendar'
    )



def _process_period( period, year, month, day ):

    if ( year == False  and month == False ):
        from_date = datetime.today()
    else:
        if ( day != False ) :
            from_date = datetime( int( year ), int( month ), int( day ) )
        else:
            from_date = datetime( int( year ), int( month ), 1 )

    if period == "day":
        to_date = from_date
        next_date = from_date + timedelta( days = 1 )
        prev_date = from_date - timedelta( days = 1 )
        repr = date( from_date, 'F j, Y' )
    elif period == "tomorrow":
        from_date = datetime.today() + timedelta( days = 1 )
        to_date = from_date
        next_date = from_date + timedelta( days = 1 )
        prev_date = from_date - timedelta( days = 1 )
        repr = date( from_date, 'F j, Y' )
    elif period == "week":
        # Adjust the start datetime to Monday or Sunday of the current week
        sub_days = from_date.isoweekday() - 1
        if sub_days > 0:
            from_date = from_date - timedelta( days = sub_days )
        to_date = from_date + timedelta( days = 7 )
        next_date = from_date + timedelta( days = 7 )
        prev_date = from_date - timedelta( days = 7 )
        repr = date( from_date, 'F j, Y' ) + ' - ' + date( to_date, 'F j, Y' )
    elif period == "month":
        cyear = from_date.year
        cmonth = from_date.month
        from_date = datetime( cyear, cmonth, 1 )
        last_day = calendar.monthrange( cyear, cmonth )[1]
        to_date = datetime( cyear, cmonth, last_day )

        next_date = from_date + relativedelta( months = +1 )
        prev_date = from_date - relativedelta( months = +1 )

        repr = date( from_date, 'F, Y' )

    return ( from_date, to_date, repr , prev_date, next_date )

@render_to( 'events/grouping.html' )
def category( request , period = 'day', date_parameter = 0 , year = False, month = False, day = False, fake_tomorrow = False ):
    request.breadcrumbs( _( 'Events' ) , '/events' )
    request.breadcrumbs( _( 'By Category' ) , request.path_info )
    dict = _process( request, lambda o: o.category, period, year, month, day )
    dict['active_tab'] = 'category'
    if fake_tomorrow:
        dict['period'] = 'tomorrow'
    return dict


@render_to( 'events/grouping.html' )
def area( request , period = 'day' , year = False, month = False, day = False, fake_tomorrow = False ):
    request.breadcrumbs( _( 'Events' ) , '/events' )
    request.breadcrumbs( _( 'By Area' ) , request.path_info )
    dict = _process( request, lambda o: o.area, period , year, month, day )
    dict['active_tab'] = 'area'
    if fake_tomorrow:
        dict['period'] = 'tomorrow'
    return dict


@render_to( 'events/grouping.html' )
def location( request , period = 'day', year = False, month = False, day = False, fake_tomorrow = False ):
    request.breadcrumbs( _( 'Events' ) , '/events' )
    request.breadcrumbs( _( 'By Location' ) , request.path_info )
    dict = _process( request, lambda o: o.location, period , year, month, day )
    dict['active_tab'] = 'location'
    if fake_tomorrow:
        dict['period'] = 'tomorrow'
    return dict


@render_to( 'events/grouping.html' )
def music( request, period = 'day' , year = False, month = False, day = False, fake_tomorrow = False ):
    request.breadcrumbs( _( 'Events' ) , '/events' )
    request.breadcrumbs( _( 'By Music' ) , request.path_info )
    dict = _process( request, lambda o: o.music, period , year, month, day )
    dict['active_tab'] = 'music'
    if fake_tomorrow:
        dict['period'] = 'tomorrow'
    return dict

@render_to( 'events/details.html' )
def detail ( request, slug, period = 'day' ):
    event = get_object_or_404( Event, slug = slug )
    request.breadcrumbs( _( 'Events' ) , '/events' )
    request.breadcrumbs( event.title , request.path_info )
    dict = _process( request, lambda o: o.category, period )
    dict['event'] = event
    dict['active_tab'] = 'category'
    return dict
