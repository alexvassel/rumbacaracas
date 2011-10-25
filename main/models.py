from django.db.models import ImageField, BooleanField, TextField, CharField, ManyToManyField, Model, ForeignKey
from preferences.models import Preferences
from django.utils.translation import ugettext_lazy as _
from sortable.models import Sortable

class MainBackgroundImage( Model ):
    title = CharField( _( 'Background image title' ), max_length = 256 )
    image = ImageField ( _( 'Background image' ), upload_to = 'images/main_background')
    url = CharField(_( 'Background click url' ), max_length=256)

    def __unicode__( self ):
        return self.title

    class Meta():
        verbose_name = "Main background image"
        verbose_name_plural = "Main background images"


class Place( Sortable ):
    title = CharField( _( 'Place title' ), max_length = 256 )
    value = CharField( _( 'Place url_name' ), max_length = 256 , blank=True)
    background_image = ForeignKey(MainBackgroundImage, blank=True, null=True)

    def __unicode__( self ):
        return self.title

    class Meta( Sortable.Meta ):
        verbose_name = _( 'Site place for background' )
        verbose_name_plural = _( 'Site places for background' )
