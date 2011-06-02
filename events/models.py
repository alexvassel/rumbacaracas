from django.db import models
from django.utils.translation import ugettext_lazy as _
from imagekit.models import ImageModel
from locations.models import Location, LocationArea, DressType, LocationMusic, WeekDay
from datetime import datetime, timedelta
import calendar
import itertools
from dateutil import rrule

EVENT_STATUSES = ( 
    ( '1', _( 'Published' ) ),
    ( '2', _( 'Blocked/ Not Published' ) ),
 )



class EventCategory( models.Model ):
    title = models.CharField( _( 'Event Category Title' ), max_length = 256 )
    def __unicode__( self ):
        return self.title
    class Meta:
        verbose_name = _( 'Event type' )
        verbose_name_plural = _( 'Event types' )


class OccurrenceManager( models.Manager ):
    use_for_related_fields = True

    def get_occuriences( self, start_date = None, end_date = None ):

        results = list()

        qs = self.filter( 
            models.Q( 
                from_date__gte = start_date,
                to_date__lte = end_date,
            ) | models.Q( 
                from_date__lte = start_date,
                to_date__gte = end_date
            ) | models.Q( 
                from_date__lte = start_date,
                to_date__lte = end_date,
                to_date__gte = start_date
            ) | models.Q( 
                from_date__gte = start_date,
                from_date__lte = end_date,
                to_date__gte = end_date
            )
        )

        for event in qs.select_related().all().filter( status = 1 ):
            #Error!!!
            rrule_start = max( event.from_date, start_date.date() )
            rrule_end = min( event.to_date, end_date.date() )

            week_days = event.repeat.all()
            if week_days:
                #fill all week days
                results.extend( [
                     ( event, tdt.date() )
                     for tdt in rrule.rrule( rrule.DAILY, dtstart = rrule_start, until = rrule_end, byweekday = [int( day.value ) for day in week_days] )
                 ] )
            else:
                #fill all days
                results.extend( [
                     ( event, tdt.date() ) for tdt in rrule.rrule( rrule.DAILY, dtstart = rrule_start, until = rrule_end )]
                )
        return results


    def get_month( self, year = None, month = None ):

        dtstart = datetime( year, month, 1 )
        last_day = calendar.monthrange( year, month )[1]
        dtend = datetime( year, month, last_day )

        results = self.get_occuriences( start_date = dtstart, end_date = dtend )
        sorted_results = sorted( results, key = lambda o: o[1].day )

        cal = calendar.monthcalendar( year, month )


        def sortList( list ):
            list.sort( key = lambda a:a[0].position, reverse = False )
            return list


        by_day = dict( [
            ( dom, sortList( list( items ) ) ) for dom, items in itertools.groupby( sorted_results, lambda o: o[1].day )
        ] )

        calendars = [[( d, by_day.get( d, [] ) ) for d in row] for row in cal]

        return calendars


from sortable.models import Sortable
#https://github.com/ff0000/django-sortablereadme

class Event( ImageModel, Sortable ):
    title = models.CharField( _( 'Event Name or Title' ), max_length = 256 )
    slug = models.SlugField ( _( 'Url name for event' ) )
    from_date = models.DateField( _( 'Event start date' ) )
    to_date = models.DateField( _( 'Event end date' ), blank = True )
    repeat = models.ManyToManyField( WeekDay , blank = True )
    category = models.ForeignKey( EventCategory )
    time = models.TimeField( _( 'Event time' ) , blank = True , null = True )
    price = models.CharField( _( 'Entrance fee, ticket, cost/price' ), max_length = 256 , blank = True )
    address = models.CharField( _( 'Address' ), max_length = 256 , blank = True )
    location = models.ForeignKey( Location , blank = True , null = True )
    music = models.ForeignKey( LocationMusic , blank = True , null = True )
    area = models.ForeignKey( LocationArea , blank = True , null = True )
    place = models.CharField( _( 'Name of venue / place' ), max_length = 256, blank = True )
    city = models.CharField( _( 'City' ), max_length = 256 , blank = True )
    phone = models.CharField( _( 'Phone' ), max_length = 256 , blank = True )
    url = models.URLField( _( 'Url' ) , blank = True )
    email = models.EmailField( _( 'Email' ) , blank = True )
    image = models.ImageField( upload_to = 'images/events', blank = True )
    user = models.CharField( 'User', max_length = 256 , blank = True )
    description = models.TextField( _( 'Event Description' ), blank = True )
    status = models.CharField( max_length = 10, choices = EVENT_STATUSES, default = 1 )
    featured = models.BooleanField( default = False )

    def view( self ):
        return u'<a target="_blank" href="/events/%s">%s</a>' % ( self.slug, _( "View on site" ) )
    view.allow_tags = True
    view.short_description = _( 'Preview' )
    class IKOptions:
        # This inner class is where we define the ImageKit options for the model
        spec_module = 'locations.specs'
        cache_dir = 'photos/'
        image_field = 'image'
        save_count_as = 'num_views'

    def __unicode__( self ):
        return self.title
    class Meta( Sortable.Meta ):
        verbose_name = _( 'Event' )
        verbose_name_plural = _( 'Events' )

    objects = OccurrenceManager()

