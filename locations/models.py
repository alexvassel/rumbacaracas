from django.db import models
from imagekit.models import ImageModel
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from socialregistration.models import FacebookProfile
from django.core.urlresolvers import reverse
from decorators import upload_to_dest
from main.modelFields import ImageRestrictedFileField
from cities.models import City
from django.db.models.signals import pre_delete, pre_save
from django.db import connections, transaction

EVENT_CITIES = []
cities = City.objects.all()
for c in cities:
    value = str(c.name)
    new_tuple = (value, _(value))
    EVENT_CITIES.append(new_tuple)
EVENT_CITIES = tuple(EVENT_CITIES)

class LocationType( models.Model ):
    title = models.CharField( _( 'Type of Venue/Club' ), max_length = 256 )
    slug = models.SlugField ( _( 'Url name for location type' ) )
    fb_type = models.CharField( _( 'Facebook open graph type' ), max_length = 256,  blank = True )
    show_in_menu = models.BooleanField(_('Show in menu'), default = True )
    def __unicode__( self ):
        return self.title
    class Meta:
        verbose_name = _( 'Location type' )
        verbose_name_plural = _( 'Location types' )
    def save(self, *args, **kwargs):
        super(LocationType, self).save(*args, **kwargs)
        super(LocationType, self).save(using = 'venezuela', *args, **kwargs)

class RestaurantType ( models.Model ):
    title = models.CharField( _( 'Type of Restaurant' ), max_length = 256 )
    def __unicode__( self ):
        return self.title
    class Meta:
        verbose_name = _( 'Type of Restaurant' )
        verbose_name_plural = _( 'Types of Restaurant' )
    def save(self, *args, **kwargs):
        super(RestaurantType, self).save(*args, **kwargs)
        super(RestaurantType, self).save(using = 'venezuela', *args, **kwargs)

class LocationArea ( models.Model ):
    title = models.CharField( _( 'Area' ), max_length = 256 )
    def __unicode__( self ):
        return self.title
    class Meta:
        verbose_name = _( 'Location area' )
        verbose_name_plural = _( 'Location areas' )
    def save(self, *args, **kwargs):
        super(LocationArea, self).save(*args, **kwargs)
        super(LocationArea, self).save(using = 'venezuela', *args, **kwargs)

class LocationMusic ( models.Model ):
    title = models.CharField( _( 'Music' ), max_length = 256 )
    def __unicode__( self ):
        return self.title
    class Meta:
        verbose_name = _( 'Location music' )
        verbose_name_plural = _( 'Location musics' )
    def save(self, *args, **kwargs):
        super(LocationMusic, self).save(*args, **kwargs)
        super(LocationMusic, self).save(using = 'venezuela', *args, **kwargs)


class DressType( models.Model ):
    title = models.CharField( _( 'Event Name or Title' ), max_length = 256 )
    def __unicode__( self ):
        return self.title
    class Meta:
        verbose_name = _( 'Dress type' )
        verbose_name_plural = _( 'Dress types' )
    def save(self, *args, **kwargs):
        super(DressType, self).save(*args, **kwargs)
        super(DressType, self).save(using = 'venezuela', *args, **kwargs)


class WeekDay( models.Model ):
    value = models.IntegerField( _( 'Value' ), max_length = 256 )
    title = models.CharField( _( 'Day title' ), max_length = 256 )
    def __unicode__( self ):
        return self.title
    class Meta:
        verbose_name = _( 'Week day' )
        verbose_name_plural = _( 'Week days' )

LOCATION_STATUSES = ( 
    ( '1', _( 'Published' ) ),
    ( '2', _( 'Blocked/ Not Published' ) ),
 )


class Location( ImageModel ):
    title = models.CharField( _( 'Name of venue/club' ), max_length = 256 )
    slug = models.SlugField ( _( 'Url name for location' ), unique=True )
    type = models.ManyToManyField( LocationType )
    restaurant = models.ManyToManyField( RestaurantType, blank = True , null = True )
    address = models.CharField( _( 'Address' ), max_length = 256 , blank = True )
    city = models.CharField( max_length = 10, choices = EVENT_CITIES, default = 1 )
    phone_1 = models.CharField( _( 'Telephone 1' ), max_length = 256 , blank = True )
    phone_2 = models.CharField( _( 'Telephone 2' ), max_length = 256 , blank = True )
    fax = models.CharField( _( 'Fax' ), max_length = 256 , blank = True )
    url = models.URLField( _( 'Url' ) , blank = True, verify_exists=False )
    email = models.EmailField( _( 'Email' ) , blank = True )
    hours_of_operation = models.CharField( _( 'Working hours' ), max_length = 256 , blank = True )
    days_of_operation = models.ManyToManyField( WeekDay , blank = True )
    area = models.ForeignKey( LocationArea , blank = True , null = True )
    music = models.ForeignKey( LocationMusic , blank = True , null = True )
    image_logo = ImageRestrictedFileField( _( 'Image logo' ), upload_to = upload_to_dest(format='uploads/locations/%Y/%m/%d') , blank = True )
    description = models.TextField( _( 'Description' ) , blank = True )
    owner = models.CharField( _( 'Owner or manager' ), max_length = 256 , blank = True )
    contact_type = models.CharField( _( 'Contact Form' ), max_length = 256 , blank = True )
    contact = models.CharField( _( 'Contact for Updates' ), max_length = 256 , blank = True )
    phones = models.CharField( _( 'Telephones' ), max_length = 256 , blank = True )
    contact_email = models.EmailField( _( 'Email' ) , blank = True )
    add_user = models.ForeignKey( User , blank = True , null = True )
    status = models.CharField( max_length = 10, choices = LOCATION_STATUSES, default = 1 )
    featured = models.BooleanField( default = False )
    datetime_added = models.DateTimeField( 'Creation Date', auto_now_add = True )

    @models.permalink
    def get_absolute_url( self ):
        """Return entry's URL"""
        return ( 'location_details', (), {
            'slug': self.slug} )

    def view( self ):
        return u'<a target="_blank" href="%s">%s</a>' % ( unicode(self.get_absolute_url(), 'utf-8'), _( "View on site" ) )

    view.allow_tags = True
    view.short_description = _( 'Preview' )
    class IKOptions:
        # This inner class is where we define the ImageKit options for the model
        spec_module = 'locations.specs'
        cache_dir = 'image_cache/'
        image_field = 'image_logo'
        save_count_as = 'num_views'

    def __unicode__( self ):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = _( 'Location' )
        verbose_name_plural = _( 'Locations' )
    
    def save(self, *args, **kwargs):
        super(Location, self).save(*args, **kwargs)
        if str(self.city) == 'Caracas':
            super(Location, self).save(using = 'venezuela', *args, **kwargs)
            
# ASSIGN A PRE_SAVE SIGNAL
def save_location_info(sender, **kwargs):
    obj = kwargs['instance']
    
    result = ''
    query = "SELECT * FROM locations_location WHERE slug='"+str(obj.slug)+"'"
    cursor = connections['venezuela'].cursor()
    cursor.execute(query)
    result = str(cursor.fetchone())
    transaction.commit_unless_managed(using='venezuela')
    if result != 'None':
        import random
        obj.slug = obj.slug+'-'+str(random.randrange(1000, 9999))
    
    
pre_save.connect(save_location_info, sender=Location)