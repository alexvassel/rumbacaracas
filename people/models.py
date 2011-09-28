from django.db import models
from django.utils.translation import ugettext_lazy as _
from decorators import upload_to_dest
from locations.models import Location
from imagekit.models import ImageModel
from django.core.urlresolvers import reverse
from main.modelFields import ImageRestrictedFileField

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
    city = models.CharField( _( 'City' ), max_length = 256 , blank = True )
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
    image = ImageRestrictedFileField( upload_to = upload_to_dest(format='uploads/people/%Y/%m/%d') )
    thumb = ImageRestrictedFileField( upload_to = upload_to_dest(format='uploads/people/%Y/%m/%d') )
    datetime_added = models.DateTimeField( 'Creation Date', auto_now_add = True )


    @models.permalink
    def get_absolute_url( self ):
        """Return entry's URL"""
        return ( 'people_slider', (), {
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
            return u'<a href="%s">%s</a>' % ( reverse('make_main',  self.event.id, self.id), _( 'Make Main' ) )
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
