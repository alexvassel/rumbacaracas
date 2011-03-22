from django.db import models
from imagekit.models import ImageModel
from django.utils.translation import ugettext_lazy as _

class LocationType( models.Model ):
    title = models.CharField( _( 'Type of Venue/Club' ), max_length = 256 )
    def __unicode__( self ):
        return self.title
    class Meta:
        verbose_name = _( 'Location type' )
        verbose_name_plural = _( 'Location types' )

class RestaurantType ( models.Model ):
    title = models.CharField( _( 'Type of Restaurant' ), max_length = 256 )
    def __unicode__( self ):
        return self.title
    class Meta:
        verbose_name = _( 'Type of Restaurant' )
        verbose_name_plural = _( 'Types of Restaurant' )

class LocationStyle ( models.Model ):
    title = models.CharField( _( 'Style of the Venue' ), max_length = 256 )
    def __unicode__( self ):
        return self.title
    class Meta:
        verbose_name = _( 'Location style' )
        verbose_name_plural = _( 'Location styles' )

class LocationArea ( models.Model ):
    title = models.CharField( _( 'Area' ), max_length = 256 )
    def __unicode__( self ):
        return self.title
    class Meta:
        verbose_name = _( 'Location area' )
        verbose_name_plural = _( 'Location areas' )

class LocationMusic ( models.Model ):
    title = models.CharField( _( 'Music' ), max_length = 256 )
    def __unicode__( self ):
        return self.title
    class Meta:
        verbose_name = _( 'Location music' )
        verbose_name_plural = _( 'Location musics' )


class DressType( models.Model ):
    title = models.CharField( _( 'Event Name or Title' ), max_length = 256 )
    def __unicode__( self ):
        return self.title
    class Meta:
        verbose_name = _( 'Dress type' )
        verbose_name_plural = _( 'Dress types' )


class Location( ImageModel ):
    title = models.CharField( _( 'Name of venue/club' ), max_length = 256 )
    slug = models.SlugField ( _( 'Url name for location' ) )
    type = models.ManyToManyField( LocationType )
    restaurant = models.ManyToManyField( RestaurantType, blank = True )
    address = models.CharField( _( 'Address' ), max_length = 256 , blank = True )
    city = models.CharField( _( 'City / District' ), max_length = 256 , blank = True )
    phone_1 = models.CharField( _( 'Telephone 1' ), max_length = 256 , blank = True )
    phone_2 = models.CharField( _( 'Telephone 2' ), max_length = 256 , blank = True )
    fax = models.CharField( _( 'Fax' ), max_length = 256 , blank = True )
    url = models.URLField( _( 'Url' ) , blank = True )
    email = models.EmailField( _( 'Email' ) , blank = True )
    hours_of_operation = models.CharField( _( 'Working hours' ), max_length = 256 , blank = True )
    style = models.ForeignKey( LocationStyle )
    area = models.ForeignKey( LocationArea , blank = True )
    music = models.ForeignKey( LocationMusic , blank = True )
    resident_dj = models.CharField( _( 'Resident DJ' ), max_length = 256 , blank = True )
    dress = models.ForeignKey( DressType , blank = True )
    capacity = models.CharField( _( 'Capacity' ), max_length = 256 , blank = True )
    image_logo = models.ImageField( _( 'Image logo' ), upload_to = 'images/locations' , blank = True )
    description = models.TextField( _( 'Description' ) , blank = True )
    owner = models.CharField( _( 'Owner or manager' ), max_length = 256 , blank = True )
    contact_type = models.CharField( _( 'Contact Form' ), max_length = 256 , blank = True )
    contact = models.CharField( _( 'Contact for Updates' ), max_length = 256 , blank = True )
    phones = models.CharField( _( 'Telephones' ), max_length = 256 , blank = True )
    contact_email = models.EmailField( _( 'Email' ) , blank = True )

    def view( self ):
        return u'<a target="_blank" href="/locations/%s">%s</a>' % ( self.slug, _( "View on site" ) )
    view.allow_tags = True
    view.short_description = _( 'Preview' )
    class IKOptions:
        # This inner class is where we define the ImageKit options for the model
        spec_module = 'locations.specs'
        cache_dir = 'photos'
        image_field = 'image_logo'
        save_count_as = 'num_views'

    def __unicode__( self ):
        return self.title

    class Meta:
        verbose_name = _( 'Location' )
        verbose_name_plural = _( 'Locations' )
