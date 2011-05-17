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



class PhotoEvent( models.Model ):
    title = models.CharField( _( 'Event title' ) , max_length = 256 )
    date = models.DateField( _( 'Event date' ) )
    category = models.CharField( 'Category', max_length = 50, choices = PHOTO_CATEGORIES )
    location = models.ForeignKey( Location , blank = True , null = True )
    author = models.CharField( _( 'Photographer or reporter' ) , max_length = 256 , blank = True )
    author_email = models.CharField( _( 'Author Email' ) , max_length = 256 , blank = True )
    city = models.CharField( _( 'City' ), max_length = 256 , blank = True )


    def import_photo( self ):
        return u'<a href="/people/import_select/%s">%s</a>' % ( str( self.id ), _( "Import page" ) )

    import_photo.allow_tags = True
    import_photo.short_description = _( 'Import page link' )

    def __unicode__( self ):
        return self.title

    class Meta:
        verbose_name = _( 'Photo Event' )
        verbose_name_plural = _( 'Photo Events' )

class Photo( ImageModel ):
    description = models.CharField( _( 'Description' ), max_length = 256 )
    event = models.ForeignKey( PhotoEvent )
    image = models.ImageField( upload_to = 'images/people' )
    thumb = models.ImageField( upload_to = 'images/people' )

    def thumb_tag( self ):
        return '<img src="%s">' % ( self.thumb.url )

    thumb_tag.allow_tags = True
    thumb_tag.short_description = _( 'Preview' )

    class IKOptions:
        spec_module = 'people.specs'
        cache_dir = 'photos/'
        image_field = 'image'

    def __unicode__( self ):
        return self.description

    class Meta:
        verbose_name = _( 'Event Photo' )
        verbose_name_plural = _( 'Event Photos' )
