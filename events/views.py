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



def _process( request, group_lambda, period , year = False, month = False, day = False, sort_category = False ):

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
    
    def sortList( list ):
        list.sort( key = lambda a:a.position, reverse = False )
        return list

    sorted_events = sorted( tmp_events , key = group_lambda )
    if sort_category:
        sorted_events = sorted( sorted_events , key = sort_category )
        
    by_group = OrderedDict( [
        ( group, sortList( list( items ) ) ) for group, items in itertools.groupby( sorted_events, group_lambda )
    ] )

    current_year = datetime.today().year
    years = range( current_year - 3, current_year + 3 )

    slider_events = Event.objects.filter( status = 1 , show_in_events_slider = True ).filter( to_date__gte = datetime.today() ).order_by( 'from_date' )[:5]

    all_locations = Location.objects.all().filter( status = 1 ).order_by( 'title' )
    all_events = Event.objects.all().filter( status = 1 ).order_by( 'title' )

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

    all_events = Event.objects.all().filter( status = 1 ).order_by( 'title' )
    request.breadcrumbs( _( 'Events' ) , reverse('event_main') )
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

    slider_events = Event.objects.filter( status = 1 , show_in_events_slider = True ).filter( to_date__gte = datetime.today() ).order_by( '?' )[:5]
    all_locations = Location.objects.all().filter( status = 1 )

    return dict( 
        today = datetime.now(),
        calendar = calendars,
        this_month = dtstart,
        repr = date( dtstart, 'F, Y' ),
        next_date = dtstart + timedelta( days = +last_day ),
        prev_date = dtstart + timedelta( days = -1 ),
        filter_date = '/' + str( year ) + '/' + str( month ),
        years = years,
        year = year,
        months = months,
        month = month,
        all_events = all_events,
        all_locations = all_locations,
        slider_events = slider_events,
        active_tab = 'calendar',
        period = period
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
    request.breadcrumbs( _( 'Events' ) , reverse('event_main') )
    request.breadcrumbs( _( 'By Category' ) , request.path_info )
    dict = _process( request, lambda o: o.category.title if o.category else None , period, year, month, day, sort_category = lambda o: o.category.position )
    dict['active_tab'] = 'category'
    if fake_tomorrow:
        dict['period'] = 'tomorrow'
    return dict


@render_to( 'events/grouping.html' )
def area( request , period = 'day' , year = False, month = False, day = False, fake_tomorrow = False ):
    request.breadcrumbs( _( 'Events' ) , reverse('event_main') )
    request.breadcrumbs( _( 'By Area' ) , request.path_info )
    dict = _process( request, lambda o: o.location.area.title if o.location.area else None, period , year, month, day )
    dict['active_tab'] = 'area'
    if fake_tomorrow:
        dict['period'] = 'tomorrow'
    return dict


@render_to( 'events/grouping.html' )
def location( request , period = 'day', year = False, month = False, day = False, fake_tomorrow = False ):
    request.breadcrumbs( _( 'Events' ) , reverse('event_main') )
    request.breadcrumbs( _( 'By Location' ) , request.path_info )
    dict = _process( request, lambda o: o.location.title if o.location else None, period , year, month, day )
    dict['active_tab'] = 'location'
    if fake_tomorrow:
        dict['period'] = 'tomorrow'
    return dict


@render_to( 'events/grouping.html' )
def music( request, period = 'day' , year = False, month = False, day = False, fake_tomorrow = False ):
    request.breadcrumbs( _( 'Events' ) , reverse('event_main') )
    request.breadcrumbs( _( 'By Music' ) , request.path_info )
    dict = _process( request, lambda o: o.music.title if o.music else None, period , year, month, day )
    dict['active_tab'] = 'music'
    if fake_tomorrow:
        dict['period'] = 'tomorrow'
    return dict

@render_to( 'events/details.html' )
def detail ( request, slug, period = 'day' ):
    event = get_object_or_404( Event, slug = slug )
    request.breadcrumbs( _( 'Events' ) , reverse('event_main') )
    request.breadcrumbs( event.title , request.path_info )
    dict = _process( request, lambda o: o.category.title if o.category else None, period )
    dict['event'] = event
    dict['active_tab'] = 'category'
    return dict


from django.contrib.auth.decorators import login_required


@login_required( login_url = '/login/' )
@render_to( 'events/add.html' )
def add( request ):
    request.breadcrumbs( _( 'Events' ) , reverse('event_main') )
    request.breadcrumbs( _( 'Add event' ) , request.path_info )

    class EventForm( ModelForm ):
        from_date = dtf(input_formats=['%d/%m/%Y',])
        to_date = dtf(input_formats=['%d/%m/%Y',], required = False)
        class Meta:
            model = Event

            location = ModelMultipleChoiceField( queryset = Location.objects.filter( status = 1 ) )
            fields = ( 
                'title',
                'from_date',
                'to_date',
                'repeat',
                'category',
                'music',
                'location',
                'place',
                'area',
                'address',

                'time',
                'price',
                'email',
                'url',
                'phone',

                'image',
                'description',
            )
        #Set required
        def clean_time(self):
            time = self.cleaned_data.get("time")
            if not time:
                raise forms.ValidationError( _("This field is required"))
            return time
        #Set required
        def clean_description(self):
            description = self.cleaned_data.get("description")
            if not description:
                raise forms.ValidationError( _("This field is required"))
            return description
        #Set required
        def clean_image(self):
            image = self.cleaned_data.get("image")
            if not image:
                raise forms.ValidationError( _("This field is required"))
            return image

        #Set required location or address and area
        def clean(self):
            cleaned_data = self.cleaned_data

            location = cleaned_data.get("location")
            address = cleaned_data.get("address")
            area = cleaned_data.get("area")

            if location or (address and area):
                return cleaned_data
            else:
                raise forms.ValidationError( _("Location or Address and Area are required"))

    if request.method == 'POST': # If the form has been submitted...
        form = EventForm( request.POST, request.FILES ) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            event = form.save( commit = False )
            event.slug = SlugifyUniquely( event.title, event.__class__)

            #set moderation status
            event.status = 2
            event.add_user = request.user
            event.save()
            form.save_m2m()
            return HttpResponseRedirect( reverse('event_main') ) # Redirect after POST
        return {
                "form": form,
                "errors": True
        }
    else:
        form = EventForm()
    return {
        'form': form,
    }

