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
import locale
from django.forms import ModelForm, ModelMultipleChoiceField
from django.template.defaultfilters import slugify
from django.http import HttpResponseRedirect
from django.forms import forms
from main.modelFields import SlugifyUniquely
from django.utils.dates import MONTHS as months
from django.core.urlresolvers import reverse
from django.forms import DateField as dtf


from people.models import PhotoEvent, Photo, PHOTO_CATEGORIES
from cities.models import City
from yourphotos.models import Photo as yourPhoto
from yourvideos.models import Video

import random

#TODO remove backported version
try:
    from collections import OrderedDict
except :
    from events.ordereddict import OrderedDict


calendar.setfirstweekday( 6 )
#MO, TU, WE, TH, FR, SA, SU

def f7( seq ):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if x not in seen and not seen_add( x )]

# filter list by city
def filterCity( list, c_name ):
    result = []
    for l in list:
        if l[0].city == c_name:
            result.append( l )
    return result

# get city name
def getCityName(slug):
    get_city = City.objects.all().filter(slug = slug)
    return get_city[0].name


def _process( request, group_lambda, period , year = False, month = False, day = False, sort_category = False , city_name = None):

    from_date, to_date, repr, prev_date, next_date = _process_period( period, year, month, day )
    
    #check supplied city name
    if city_name == None:
        c_name = 'all cities'
    else:
        c_name = getCityName(city_name)

    
    events = Event.objects.get_occuriences( start_date = from_date, end_date = to_date )
    if city_name != None:
        events = filterCity(events, c_name.capitalize())
    upcoming_events = Event.objects.get_occuriences( start_date = datetime.today(), end_date = datetime.today() + timedelta(365), repeat_count = 1)

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
    
    def sortList( list ):
        list.sort( key = lambda a:a.position, reverse = False )
        return list

    sorted_events = sorted( tmp_events , key = group_lambda )
    if sort_category:
        sorted_events = sorted( sorted_events , key = sort_category )
        
    by_group = list( [
        ( group, sortList( list( items ) ) ) for group, items in itertools.groupby( sorted_events, group_lambda )
    ] )

    #Add special group for top events
    special_group = list()
    for group in by_group:
        group_top_items = group[1][0:4]
        special_group.extend(group_top_items)
    random.shuffle(special_group)

    if special_group:
        by_group = list([(_("Recommended Events"), special_group[:4])]) + by_group

    current_year = datetime.today().year
    years = range( current_year - 3, current_year + 3 )


    #Get slider
    if city_name == None:
        sliders_qs = Event.objects.filter( status = 1 , show_in_events_slider = True )
    else:
        sliders_qs = Event.objects.filter( status = 1 , show_in_events_slider = True, city = c_name )
    slider_events = [event for event, dt in Event.objects.get_occuriences(qs=sliders_qs, start_date = from_date, end_date = to_date )]
    slider_events = f7(slider_events)    
    random.shuffle(slider_events)
    
    #if not slider_events:
     #   slider_events = Event.objects.filter( status = 1 , show_in_events_slider = True ).filter( to_date__gte = datetime.today() ).order_by( 'from_date' )

    all_locations = Location.objects.all().filter( status = 1 ).order_by( 'title' )
    #all_events = Event.objects.all().filter( status = 1 ).order_by( 'title' )

    #Seems like wrong
    year = from_date.year
    month = from_date.month
    day = from_date.day

    upcoming_events = sorted( upcoming_events, key = lambda o: o[1], reverse=False)

    if period != "month":
        filter_date = '/' + str( year ) + '/' + str( month ) + '/' + str( day )
    else:
        filter_date = '/' + str( year ) + '/' + str( month )
        
    # HERE GOES PEOPLE EVENTS #
    people_groups = []
    if city_name == None:
        for group, description in PHOTO_CATEGORIES:
            events = PhotoEvent.objects.filter( status = 1 ).filter( city = group ).filter( category = 'outside' ).order_by( '-date' )
            if events:
                latest_event_photo = events[0]
                people_groups.append( ( group, description, latest_event_photo, events, ) )
    else:
        events = PhotoEvent.objects.filter( status = 1 ).filter( city = city_name ).filter( category = 'outside' ).order_by( '-date' )
        if events:
            latest_event_photo = events[0]
            people_groups.append( ( city_name, city_name, latest_event_photo, events, ) )
            
    if city_name != None:
        random.shuffle(people_groups)
        
    people_latest = PhotoEvent.objects.filter( status = 1 ).filter( category = 'outside' ).latest( 'date' )
    ###########################
    
    
    # HERE GOES LOCAL PHOTOS #
    l_photos = yourPhoto.objects.filter( status = 1 ).order_by( '-datetime_added' )
    ##########################
    
    # HERE GOES VIDEOS #
    videos = Video.objects.filter( status = 1 ).order_by( '-datetime_added' )[:5]
    ####################
    
    return {'city_name': c_name, 'filter_date': filter_date, 'all_locations': all_locations, 'all_events': upcoming_events,
            'groups': by_group[:1], 'slider_events': slider_events[:5], 'years': years, 'months': months, 'repr': repr, 'year': year,
            'month': month, 'period': period, 'prev_date': prev_date, 'next_date': next_date, 'closest_dates': tmp_closest_dates,
            'people_groups': people_groups[:1], 'people_latest': people_latest, 'local_photos': l_photos, 'videos': videos}






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


@render_to( 'cities/cities.html' )
def index( request , period = 'day' , year = False, month = False, day = False, fake_tomorrow = False ):
    request.breadcrumbs( _( 'Cities' ) , reverse('city_index') )
    request.breadcrumbs( _( 'All cities' ) , request.path_info )
    dict = _process( request, lambda o: o.location.area.title if (o.location and o.location.area) else None, period , year, month, day )
    dict['active_tab'] = 'area'
    if fake_tomorrow:
        dict['period'] = 'tomorrow'
    return dict


@render_to( 'cities/cities.html' )
def city_index( request , city, period = 'day', year = False, month = False, day = False, fake_tomorrow = False ):
    request.breadcrumbs( _( 'Cities' ) , reverse('city_index') )
    request.breadcrumbs( _( getCityName(city) ) , request.path_info )
    dict = _process( request, lambda o: o.location.title if o.location else None, period , year, month, day, city_name = city)
    dict['active_tab'] = 'location'
    if fake_tomorrow:
        dict['period'] = 'tomorrow'
    return dict