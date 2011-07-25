from django.db import models
from zinnia.models import EntryAbstractClass
from django.utils.translation import ugettext_lazy as _

from zinnia.settings import UPLOAD_TO

class MyEntry( EntryAbstractClass ):
    short = models.TextField( _( 'short description' ), max_length=50 )
    source = models.CharField( _( 'source' ), blank = True, max_length = 255 )
    author = models.CharField( _( 'author' ), blank = True, max_length = 255 )
    slider_image = models.ImageField( _( 'Slider image 619x258' ), upload_to = 'images/slider' , blank = True )
    show_in_main_slider = models.BooleanField( _( 'Show in Main Slider' ), default = False )

    class IKOptions:
        # This inner class is where we define the ImageKit options for the model
        spec_module = 'yourphotos.specs'
        cache_dir = 'blog/'
        image_field = 'image'
        save_count_as = 'num_views'

    class Meta:
        abstract = True
