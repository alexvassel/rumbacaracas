from django.db import models
from django.db.models import Model
from django.utils.translation import ugettext_lazy as _
from decorators import upload_to_dest
from locations.models import Location
from imagekit.models import ImageModel
from django.core.urlresolvers import reverse
from main.modelFields import ImageRestrictedFileField
from cities.models import City

EVENT_CITIES = []
cities = City.objects.all()
for c in cities:
    value = unicode(c.name)
    new_tuple = (value, _(value))
    EVENT_CITIES.append(new_tuple)
EVENT_CITIES = tuple(EVENT_CITIES)

PHOTO_CATEGORIES = ( 
    ( 'rumbas', _( 'Rumbas' ) ),
    ( 'concerts', _( 'Events and Concerts' ) ),
    ( 'clubs', _( 'Clubs and Bars' ) ),
    ( 'launches', _( 'Launches and More' ) ),
    ( 'fashion', _( 'Fashion ' ) ),
    ( 'outside', _( 'Outside caracas' ) ),
 )


PEOPLE_STATUSES = ( 
    ( '1', _( 'Published' ) ),
    ( '2', _( 'Hidden/ Not Published' ) ),
 )


class PhotoEvent( ImageModel ):
    title = models.CharField( _( 'Event title' ) , max_length = 256 )
    slug = models.SlugField ( _( 'Url name for event' ),unique=True )
    date = models.DateField( _( 'Event date' ) )
    category = models.CharField( 'Category', max_length = 50, choices = PHOTO_CATEGORIES )
    article = models.TextField( _( 'Description' ) , blank = True )
    location = models.ForeignKey( Location , blank = True , null = True )
    author = models.CharField( _( 'Photographer or reporter' ) , max_length = 256 , blank = True )
    author_email = models.CharField( _( 'Author Email' ) , max_length = 256 , blank = True )
    city = models.CharField( max_length = 20, choices = EVENT_CITIES, default = 1 )
    image = ImageRestrictedFileField( upload_to = upload_to_dest(format='uploads/people/%Y/%m/%d'), blank = True )
    status = models.CharField( max_length = 10, choices = PEOPLE_STATUSES, default = 2 )
    datetime_added = models.DateTimeField( 'Creation Date', auto_now_add = True )

    @models.permalink
    def get_absolute_url( self ):
        """Return entry's URL"""
        return ( 'people_details', (), {
            'slug': self.slug} )

    def __unicode__( self ):
        return self.title

    class Meta:
        verbose_name = _( 'Photo Event' )
        verbose_name_plural = _( 'Photo Events' )

    class IKOptions:
        spec_module = 'people.specs'
        cache_dir = 'image_cache/'
        image_field = 'image'

class Photo( ImageModel ):
    description = models.CharField( _( 'Description' ), max_length = 256 )
    event = models.ForeignKey( PhotoEvent )
    image = ImageRestrictedFileField( upload_to = upload_to_dest(format='uploads/people/%Y/%m/%d'), max_length = 110 )
    thumb = ImageRestrictedFileField( upload_to = upload_to_dest(format='uploads/people/%Y/%m/%d') )
    datetime_added = models.DateTimeField( 'Creation Date', auto_now_add = True )


    @models.permalink
    def get_absolute_url( self ):
        """Return entry's URL"""
        return ( 'people_slider', (), { 'slug' : self.event.slug,
            'photo_id': self.id} )

    def thumb_tag( self ):
        if self.id:
            return '<img src="%s">' % ( self.thumb.url )
        else:
            return ""

    thumb_tag.allow_tags = True
    thumb_tag.short_description = _( 'Preview' )

    def make_main_tag( self ):
        if self.id:
            return u'<a href="%s">%s</a>' % ( reverse('people_make_main', None,  (self.event.id, self.id) ), _( 'Make Main' ) )
        else:
            return ""

    make_main_tag.allow_tags = True
    make_main_tag.short_description = _( 'Make Main' )

    def get_next( self ):
        next_rows = Photo.objects.order_by( 'datetime_added', 'id' ).filter( event = self.event, datetime_added__gte = self.datetime_added, pk__gt = self.id )
        if ( next_rows ):
            return next_rows[0]
        else:
            return Photo.objects.filter( event = self.event ).order_by( 'datetime_added', 'id' )[0]

    def get_prev( self ):
        prev_rows = Photo.objects.order_by( '-datetime_added', '-id' ).filter( event = self.event, datetime_added__lte = self.datetime_added , pk__lt = self.id )
        if ( prev_rows ):
            return prev_rows[0]
        else:
            return Photo.objects.filter( event = self.event ).order_by( '-datetime_added', '-id' )[0]

    class IKOptions:
        spec_module = 'people.specs'
        cache_dir = 'image_cache/'
        image_field = 'image'

    def __unicode__( self ):
        return self.description

    class Meta:
        verbose_name = _( 'Event Photo' )
        verbose_name_plural = _( 'Event Photos' )



REQUEST_CATEGORIES = (
    ( 'corporate', _( 'Corporate' ) ),
    ( 'birthday', _( 'Birthday' ) ),
    ( 'Wedding', _( 'Wedding (civil/ecclesiastical)' ) ),
    ( 'graduation', _( 'Graduation' ) ),
    ( 'others', _( 'Others' ) ),
)


class EventRequest( Model ):
    name = models.CharField( _( 'Your name' ) , max_length = 256 )
    email = models.EmailField( _( 'Your Email' ) , max_length = 256)
    phone = models.CharField( _( 'Telephone' ), max_length = 256 , blank = True )
    fax = models.CharField( _( 'Fax' ), max_length = 256 , blank = True )

    category = models.CharField( _('Type of event'), max_length = 50, choices = REQUEST_CATEGORIES )
    date = models.DateField( _( 'Event date' ) )
    time = models.TimeField( _( 'Event time' ), max_length = 64)

    address = models.TextField( _( 'Event location' ))
    city = models.CharField( _( 'City' ), max_length = 256)
    information = models.TextField( _( 'Additional information' ) , blank = True )
    datetime_added = models.DateTimeField( 'Creation Date', auto_now_add = True )


    def __unicode__( self ):
        return self.name

    class Meta:
        verbose_name = _( 'Hiring request' )
        verbose_name_plural = _( 'Hiring requests' )
