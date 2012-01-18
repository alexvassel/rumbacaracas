from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from decorators import upload_to_dest
from main.modelFields import ImageRestrictedFileField

# Create your models here.
class City( models.Model ):
    name = models.CharField( _( 'Name of the city' ), max_length = 256 )
    slug = models.SlugField ( _( 'Url name for city' ) )
    show_in_menu = models.BooleanField(_('Show in menu'), default = True )
    def __unicode__( self ):
        return self.name
    class Meta:
        verbose_name = _( 'City' )
        verbose_name_plural = _( 'Cities' )
