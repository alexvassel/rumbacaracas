from django.db import models
from socialregistration.models import FacebookProfile
from django.utils.translation import ugettext_lazy as _
from imagekit.models import ImageModel
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from decorators import upload_to_dest
from main.modelFields import ImageRestrictedFileField

PHOTO_STATUSES = ( 
    ( '1', _( 'Published' ) ),
    ( '2', _( 'Blocked/ Not Published' ) ),
 )

PHOTO_CATEGORIES = ( 
    ( 'sexy', _( 'Sexy' ) ),
    ( 'rumbas', _( 'Rumbas' ) ),
    ( 'amigos', _( 'Amigos' ) ),
    ( 'humor', _( 'Humor' ) ),
 )


class Photo( ImageModel ):
    user = models.ForeignKey( User )
    description = models.CharField( _( 'Description' ), max_length = 256 )
    category = models.CharField( 'Category', max_length = 10, choices = PHOTO_CATEGORIES, blank = True )
    image = ImageRestrictedFileField( upload_to = upload_to_dest(format='uploads/yourphotos/%Y/%m/%d') )
    status = models.CharField( max_length = 10, choices = PHOTO_STATUSES, default = 2 )
    datetime_added = models.DateTimeField( 'Creation Date', auto_now_add = True )
    def thumb( self ):
        return '<img src="%s">' % ( self.thumbnail.url )
    thumb.allow_tags = True
    thumb.short_description = _( 'Preview' )

    @models.permalink
    def get_absolute_url( self ):
        """Return entry's URL"""
        return ( 'yourphoto_details', (), {
            'id': self.id} )

    def get_user_link ( self ):
        try :
            facebook_user = FacebookProfile.objects.get( user = self.user )
            return mark_safe( u'<fb:name uid="%s"  target="_blank" />' % ( facebook_user.uid ) )
        except FacebookProfile.DoesNotExist:
            return mark_safe( self.user.username )

    class IKOptions:
        # This inner class is where we define the ImageKit options for the model
        spec_module = 'yourphotos.specs'
        cache_dir = 'image_cache/'
        image_field = 'image'
        save_count_as = 'num_views'


    def get_next( self ):
        next_rows = Photo.objects.order_by( 'datetime_added', 'id' ).filter( status = 1 ).filter( datetime_added__gte = self.datetime_added, pk__gt = self.id )
        if ( next_rows ):
            return next_rows[0]
        else:
            return Photo.objects.filter( status = 1 ).order_by( 'datetime_added', 'id' )[0]

    def get_prev( self ):
        prev_rows = Photo.objects.filter( status = 1 ).order_by( '-datetime_added', '-id' ).filter( datetime_added__lte = self.datetime_added , pk__lt = self.id )
        if ( prev_rows ):
            return prev_rows[0]
        else:
            return Photo.objects.filter( status = 1 ).order_by( '-datetime_added', '-id' )[0]

    def __unicode__( self ):
        return self.description
    class Meta:
        verbose_name = _( 'Your Photo' )
        verbose_name_plural = _( 'Your Photos' )
