from django.db import models
from imagekit.models import ImageModel
from zinnia.models import EntryAbstractClass
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import smart_str
from django.utils.encoding import force_unicode
from django.contrib.auth.models import User
from zinnia.settings import UPLOAD_TO
from main.modelFields import ImageRestrictedFileField
import datetime
import string,random
import os


def upload_to_profile(instance, filename):
    format = 'uploads/author_profiles/%Y/%m/%d/%H%M%S'
    prefix = os.path.normpath(force_unicode(datetime.datetime.now().strftime(smart_str(format))))
    postfix = '%s%s' % (
        string.join(random.sample(string.ascii_letters + string.digits, 5), ''),
        os.path.splitext(filename)[-1],
    )
    filepath = '%s_%s' % (prefix, postfix)
    return filepath

class AuthorProfile( ImageModel ):
    profile_photo= ImageRestrictedFileField(upload_to = upload_to_profile , null=True, blank = True )
    about_author = models.TextField( _( 'About Author' ), blank = True, null = True )
    user = models.OneToOneField( User , blank = False , null = False )
    class IKOptions:
        # This inner class is where we define the ImageKit options for the model
        spec_module = 'yourphotos.specs'
        cache_dir = 'image_cache/'
        image_field = 'profile_photo'
        save_count_as = 'num_views'
    
    def __unicode__( self ):
        return self.user.first_name + " " + self.user.last_name
    
    
    @models.permalink
    def get_absolute_url( self ):
        """Return entry's URL"""
        return ( 'ath_profile', (), {
            'profile_id': self.user.username} )
    
    class Meta:
        verbose_name = _( 'Author Profile' )
        verbose_name_plural = _( 'Author Profiles' )


class MyEntry( EntryAbstractClass ):
    short = models.TextField( _( 'short description' ), max_length=50 )
    source = models.CharField( _( 'source' ), blank = True, max_length = 255 )
    author_profile = models.ForeignKey( AuthorProfile , blank = True , null = True, verbose_name="Author Profile" )
    author = models.CharField( _( 'author' ), blank = True, max_length = 255 )
    slider_image = ImageRestrictedFileField( _( 'Slider image 619x258' ), upload_to = UPLOAD_TO , blank = True )
    show_in_main_slider = models.BooleanField( _( 'Show in Main Slider' ), default = False )
    preview_as_image = models.BooleanField( _( 'Show image as preview' ), default = False )
    preview_image = ImageRestrictedFileField( _( 'Preview image 600px width' ), upload_to = UPLOAD_TO , blank = True )
    class IKOptions:
        # This inner class is where we define the ImageKit options for the model
        spec_module = 'yourphotos.specs'
        cache_dir = 'image_cache/'
        image_field = 'image'
        save_count_as = 'num_views'

    class Meta:
        abstract = True



ZINNIA_UPLOAD_TO = ""

def unique_filepath(instance, filename):

        fname, ext = os.path.splitext(filename)

        if hasattr(instance, human_readable_field) and \
            getattr(instance, human_readable_field) and \
            getattr(instance, human_readable_field) != '':
            fname_chunk = getattr(instance, human_readable_field)
        else:
            fname_chunk = uuid.uuid4()

        filename = "%s%s" % (fname_chunk, ext.lower())
        return os.path.join(path, filename)


def upload_to(instance, filename):
    format = 'uploads/news/%Y/%m/%d/%H%M%S'
    prefix = os.path.normpath(force_unicode(datetime.datetime.now().strftime(smart_str(format))))
    postfix = '%s%s' % (
        string.join(random.sample(string.ascii_letters + string.digits, 5), ''),
        os.path.splitext(filename)[-1],
    )
    filepath = '%s_%s' % (prefix, postfix)
    return filepath




    
    