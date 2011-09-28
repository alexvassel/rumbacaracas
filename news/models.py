# The model
from django.db import models
from django.utils.translation import ugettext_lazy as _

from zinnia.models import Entry
from zinnia.settings import UPLOAD_TO
from main.modelFields import ImageRestrictedFileField

class EntryImage( models.Model ):
    """Image Model"""
    entry = models.ForeignKey( Entry, verbose_name = _( 'entry' ) )
    image = ImageRestrictedFileField( _( 'Additional image' ), upload_to = UPLOAD_TO )
    def __unicode__( self ):
        return self.image.url

from preferences.models import Preferences


SLIDER_STATUSES = ( 
    ( '1', _( 'Only Events' ) ),
    ( '2', _( 'Only News' ) ),
    ( '3', _( 'News and Events' ) ),
 )


class MainSliderPreferences( Preferences ):
    __module__ = 'preferences.models'
    status = models.CharField( _( "Show in Main Slider" ), max_length = 128, choices = SLIDER_STATUSES, blank = True, null = True )

    class Meta():
        verbose_name = "Main slider preferences"
        verbose_name_plural = "Main slider preferences"
