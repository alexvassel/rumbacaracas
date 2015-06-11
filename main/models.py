from django.db.models import ImageField, BooleanField, TextField, CharField, ManyToManyField, Model, ForeignKey
from preferences.models import Preferences
from django.utils.translation import ugettext_lazy as _
from sortable.models import Sortable
from django.contrib.contenttypes.models import ContentType
from django.db.models.fields import IntegerField

class MainBackgroundImage( Model ):
    title = CharField( _( 'Background image title' ), max_length = 256 )
    image = ImageField ( _( 'Background image' ), upload_to = 'images/main_background')
    url = CharField(_( 'Background click url' ), max_length=256, blank=True)

    def __unicode__( self ):
        return self.title

    class Meta():
        verbose_name = _("Main background image")
        verbose_name_plural = _("Main background images")


class CursorImage( Model ):
    title = CharField( _( 'Cursor image title' ), max_length = 256 )
    image = ImageField ( _( 'Cursor image' ), upload_to = 'images/cursors')

    def __unicode__( self ):
        return self.title

    class Meta():
        verbose_name = _("Cursor image")
        verbose_name_plural = _("Cursor images")

class Place( Sortable ):
    title = CharField( _( 'Place title' ), max_length = 256 )
    value = CharField( _( 'Place url_name' ), max_length = 256 , blank=True)
    background_image = ForeignKey(MainBackgroundImage, blank=True, null=True)
    cursor_image = ForeignKey(CursorImage, blank=True, null=True)

    def __unicode__( self ):
        return self.title

    class Meta( Sortable.Meta ):
        verbose_name = _( 'Site place for background, cursor' )
        verbose_name_plural = _( 'Site places for background, cursor' )

class MostViewed( Model ):
    content_type = ForeignKey(ContentType, blank=False, null=False)
    content_type_object_id = IntegerField(null=False, blank=False)
    no_of_views = IntegerField(null=False, blank=False)
    
    class Meta():
        verbose_name = _("Most Viewed")
        verbose_name_plural = _("Most Viewed")
    