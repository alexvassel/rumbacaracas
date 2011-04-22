from django.db import models
from socialregistration.models import FacebookProfile
from django.utils.translation import ugettext_lazy as _
from imagekit.models import ImageModel
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

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
    image = models.ImageField( upload_to = 'images/yourphotos' )
    status = models.CharField( max_length = 10, choices = PHOTO_STATUSES, default = 2 )
    datetime_added = models.DateTimeField( 'Creation Date', auto_now_add = True )
    def thumb( self ):
        return '<img src="%s">' % ( self.thumbnail.url )
    thumb.allow_tags = True
    thumb.short_description = _( 'Preview' )

    def get_user_link ( self ):
        facebook_user = FacebookProfile.objects.get( user = self.user )
        if facebook_user:
            return mark_safe( u'<fb:name uid="%s" />' % ( facebook_user.uid ) )
        else:
            return mark_safe( self.user )

    class IKOptions:
        # This inner class is where we define the ImageKit options for the model
        spec_module = 'yourphotos.specs'
        cache_dir = 'photos/'
        image_field = 'image'
        save_count_as = 'num_views'


    def get_next( self ):
        next_rows = Photo.objects.order_by( 'datetime_added', 'id' ).filter( status = 1 ).filter( datetime_added__gte = self.datetime_added, pk__gt = self.id )
        if ( next_rows ):
            return next_rows[0]
        else:
            return Photo.objects.filter( status = 1 ).order_by( 'datetime_added' )[0]

    def get_prev( self ):
        prev_rows = Photo.objects.filter( status = 1 ).order_by( '-datetime_added', '-id' ).filter( datetime_added__lte = self.datetime_added , pk__lt = self.id )
        if ( prev_rows ):
            return prev_rows[0]
        else:
            return Photo.objects.filter( status = 1 ).latest( 'datetime_added' )
            return False

    def __unicode__( self ):
        return self.description
    class Meta:
        verbose_name = _( 'Your Photo' )
        verbose_name_plural = _( 'Your Photos' )
