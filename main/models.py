from django.db import models
from django.utils.translation import ugettext_lazy as _
from imagekit.models import ImageModel
from datetime import datetime

SLIDE_STATUSES = ( 
    ( '1', _( 'Enabled' ) ),
    ( '2', _( 'Disabled' ) ),
 )

class PublishedManager( models.Manager ):
    def published_slides( self ):
        """Return only the entries published"""
        now = datetime.now()
        return self.filter( status = 1,
           start_publication__lte = now,
           end_publication__gt = now )

#Rules
# Get 4 slides where slide is enabled and date is ok, sort by random.  
class Slide( ImageModel ):
    title = models.CharField( _( 'Title' ), max_length = 256 )
    link = models.CharField( _( 'Link' ), max_length = 256 )
    description = models.TextField( _( 'Description' ), max_length = 512 )
    image = models.ImageField( upload_to = 'images/slider' )
    status = models.CharField( max_length = 10, choices = SLIDE_STATUSES, default = 1 )

    start_publication = models.DateTimeField( _( 'start publication' ), default = datetime.now )
    end_publication = models.DateTimeField( _( 'end publication' ), default = datetime( 2042, 3, 15 ) )

    datetime_added = models.DateTimeField( 'Creation Date', auto_now_add = True )


    @property
    def is_actual( self ):
        """Check if an entry is within publication period"""
        now = datetime.now()
        return now >= self.start_publication and now < self.end_publication

    @property
    def is_visible( self ):
        """Check if an entry is visible on site"""
        return self.is_actual and self.status == '1'


    objects = PublishedManager()

    class IKOptions:
        # This inner class is where we define the ImageKit options for the model
        spec_module = 'yourphotos.specs'
        cache_dir = 'photos/'
        image_field = 'image'
        save_count_as = 'num_views'

    def __unicode__( self ):
        return self.title
    class Meta:
        verbose_name = _( 'Slide' )
        verbose_name_plural = _( 'Slides' )
