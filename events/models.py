from django.db import models
from django.utils.translation import ugettext_lazy as _
from imagekit.models import ImageModel
from locations.models import Location, LocationArea, DressType

class EventCategory( models.Model ):
    title = models.CharField( _( 'Event Category Title' ), max_length = 256 )
    def __unicode__( self ):
        return self.title
    class Meta:
        verbose_name = _( 'Event type' )
        verbose_name_plural = _( 'Event types' )

class WeekDay( models.Model ):
    value = models.CharField( _( 'Value' ), max_length = 256 )
    title = models.CharField( _( 'Day title' ), max_length = 256 )
    def __unicode__( self ):
        return self.title
    class Meta:
        verbose_name = _( 'Week day' )
        verbose_name_plural = _( 'Week days' )


class Event( ImageModel ):
    title = models.CharField( _( 'Event Name or Title' ), max_length = 256 )
    slug = models.SlugField ( _( 'Url name for event' ) )
    from_date = models.DateField( _( 'Event start date' ) )
    to_date = models.DateField( _( 'Event end date' ) )
    repeat = models.ManyToManyField( WeekDay , blank = True )
    category = models.ForeignKey( EventCategory )
    time = models.TimeField( _( 'Event time' ) , blank = True , null = True )
    dress = models.ForeignKey( DressType , blank = True , null = True )
    price = models.CharField( _( 'Entrance fee, ticket, cost/price' ), max_length = 256 , blank = True )
    address = models.CharField( _( 'Address' ), max_length = 256 , blank = True )
    location = models.ForeignKey( Location , blank = True , null = True )
    area = models.ForeignKey( LocationArea , blank = True , null = True )
    place = models.CharField( _( 'Name of venue / place' ), max_length = 256, blank = True )
    city = models.CharField( _( 'City' ), max_length = 256 , blank = True )
    url = models.URLField( _( 'Url' ) , blank = True )
    email = models.EmailField( _( 'Email' ) , blank = True )
    sort_order = models.IntegerField( _( 'Hierarchy ' ), blank = True, null = True )
    image = models.ImageField( upload_to = 'images/events', blank = True )
    user = models.CharField( 'User', max_length = 256 , blank = True )
    description = models.TextField( _( 'Event Description' ), blank = True )

    def view( self ):
        return u'<a target="_blank" href="/events/%s">%s</a>' % ( self.slug, _( "View on site" ) )
    view.allow_tags = True
    view.short_description = _( 'Preview' )
    class IKOptions:
        # This inner class is where we define the ImageKit options for the model
        spec_module = 'locations.specs'
        cache_dir = 'photos'
        image_field = 'image'
        save_count_as = 'num_views'

    def __unicode__( self ):
        return self.title
    class Meta:
        verbose_name = _( 'Event' )
        verbose_name_plural = _( 'Events' )
