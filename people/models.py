from django.db import models
from django.utils.translation import ugettext_lazy as _
from locations.models import Location
from imagekit.models import ImageModel

PHOTO_CATEGORIES = ( 
    ( 'rumbas', _( 'Rumbas' ) ),
    ( 'concerts', _( 'Events and Concerts' ) ),
    ( 'clubs', _( 'Clubs and Bars' ) ),
    ( 'launches', _( 'Launches and More' ) ),
    ( 'fashion', _( 'Fashion ' ) ),
    ( 'outside', _( 'Outside Bogota' ) ),
 )



class PhotoEvent( ImageModel ):
    title = models.CharField( _( 'Event title' ) , max_length = 256 )
    slug = models.SlugField ( _( 'Url name for event' ) )
    date = models.DateField( _( 'Event date' ) )
    category = models.CharField( 'Category', max_length = 50, choices = PHOTO_CATEGORIES )
    article = models.TextField( _( 'Description' ) , blank = True )
    location = models.ForeignKey( Location , blank = True , null = True )
    author = models.CharField( _( 'Photographer or reporter' ) , max_length = 256 , blank = True )
    author_email = models.CharField( _( 'Author Email' ) , max_length = 256 , blank = True )
    city = models.CharField( _( 'City' ), max_length = 256 , blank = True )
    image = models.ImageField( upload_to = 'images/people', blank = True )
    datetime_added = models.DateTimeField( 'Creation Date', auto_now_add = True )

    def import_photo( self ):
        return u'<a href="/people/import_select/%s">%s</a>' % ( str( self.id ), _( "Import page" ) )

    import_photo.allow_tags = True
    import_photo.short_description = _( 'Import page link' )

    def __unicode__( self ):
        return self.title

    class Meta:
        verbose_name = _( 'Photo Event' )
        verbose_name_plural = _( 'Photo Events' )

    class IKOptions:
        spec_module = 'people.specs'
        cache_dir = 'photos/'
        image_field = 'image'

class Photo( ImageModel ):
    description = models.CharField( _( 'Description' ), max_length = 256 )
    event = models.ForeignKey( PhotoEvent )
    image = models.ImageField( upload_to = 'images/people' )
    thumb = models.ImageField( upload_to = 'images/people' )
    datetime_added = models.DateTimeField( 'Creation Date', auto_now_add = True )

    def thumb_tag( self ):
        if self.id:
            return '<img src="%s">' % ( self.thumb.url )
        else:
            return ""

    thumb_tag.allow_tags = True
    thumb_tag.short_description = _( 'Preview' )

    def make_main_tag( self ):
        if self.id:
            return u'<a href="/people/make_main/%s/%s">%s</a>' % ( self.event.id, self.id, _( 'Make Main' ) )
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
        cache_dir = 'photos/'
        image_field = 'image'

    def __unicode__( self ):
        return self.description

    class Meta:
        verbose_name = _( 'Event Photo' )
        verbose_name_plural = _( 'Event Photos' )