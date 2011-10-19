from django.db.models import ImageField
from preferences.models import Preferences
from django.utils.translation import ugettext_lazy as _

class MainBackgroundPreferences( Preferences ):
    __module__ = 'preferences.models'
    background_image = ImageField ( _( 'Main background image' ),upload_to = 'images/main_background')

    class Meta():
        verbose_name = "Main background image"
        verbose_name_plural = "Main background images"
