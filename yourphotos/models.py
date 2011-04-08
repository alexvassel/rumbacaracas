from django.db import models
from django.utils.translation import ugettext_lazy as _
from imagekit.models import ImageModel

class PhotoCategory( models.Model ):
    title = models.CharField( _( 'Your Photo Category Title' ), max_length = 256 )
    def __unicode__( self ):
        return self.title
    class Meta:
        verbose_name = _( 'Your Photo Category' )
        verbose_name_plural = _( 'Your Photo Categories' )


PHOTO_STATUSES = ( 
    ( '1', 'Published' ),
    ( '2', 'Blocked/ Not Published' ),
 )

class Photo( ImageModel ):
    user = models.CharField( _( 'User' ), max_length = 256 )
    description = models.CharField( _( 'Your Photo Description' ), max_length = 256 )
    category = models.ForeignKey( PhotoCategory )
    image = models.ImageField( upload_to = 'images/myphotos', blank = True )
    status = models.CharField( max_length = 10, choices = PHOTO_STATUSES )
    def thumb( self ):
        return '<img src="%s">' % ( self.thumbnail.url )
    thumb.allow_tags = True
    thumb.short_description = _( 'Preview' )

    class IKOptions:
        # This inner class is where we define the ImageKit options for the model
        spec_module = 'yourphotos.specs'
        cache_dir = 'photos/'
        image_field = 'image'
        save_count_as = 'num_views'

    def __unicode__( self ):
        return self.description
    class Meta:
        verbose_name = _( 'Your Photo' )
        verbose_name_plural = _( 'Your Photos' )
