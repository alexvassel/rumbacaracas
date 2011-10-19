from django.db.models import ImageField, BooleanField, TextField, CharField, ManyToManyField, Model
from preferences.models import Preferences
from django.utils.translation import ugettext_lazy as _

class Places( Model ):
    value = CharField( _( 'Place url_name' ), max_length = 256 , blank=True)
    title = CharField( _( 'Place title' ), max_length = 256 )
    def __unicode__( self ):
        return self.title
    class Meta:
        ordering = ['title']
        verbose_name = _( 'Site place for background' )
        verbose_name_plural = _( 'Site places for background' )


class MainBackgroundPreferences( Preferences ):
    __module__ = 'preferences.models'
    places = ManyToManyField( Places, blank = True , null = True )
    background_image = ImageField ( _( 'Main background image' ), upload_to = 'images/main_background')
    url = CharField(_( 'Main background url' ), max_length=256)

    class Meta():
        verbose_name = "Main background image"
        verbose_name_plural = "Main background images"
