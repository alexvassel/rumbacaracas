from django.db import models
from socialregistration.models import FacebookProfile
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from modelFields import YoutubeField

VIDEO_STATUSES = ( 
    ( '1', _( 'Published' ) ),
    ( '2', _( 'Blocked/ Not Published' ) ),
 )

from yourvideos.templatetags.youtube import youtube_img_from_id, youtube_video_from_id
class Video( models.Model ):
    user = models.ForeignKey( User , blank = True, null = True )
    youtube_id = YoutubeField( _( 'Youtube link or Youtube Id' ), max_length = 256 )
    description = models.CharField( _( 'Description' ), max_length = 256, blank = True )
    status = models.CharField( max_length = 10, choices = VIDEO_STATUSES, default = 2 )
    datetime_added = models.DateTimeField( 'Creation Date', auto_now_add = True )

    def thumb( self ):
        return '<img src="%s">' % ( youtube_img_from_id( self.youtube_id ) )
    thumb.allow_tags = True
    thumb.short_description = _( 'Preview' )

    def get_thumb_src(self):
        return youtube_img_from_id( self.youtube_id )

    def video( self ):
        return  youtube_video_from_id( self.youtube_id )
    video.allow_tags = True
    video.short_description = _( 'Video Preview' )

    @models.permalink
    def get_absolute_url( self ):
        """Return entry's URL"""
        return ( 'video_details', (), {
            'id': self.id} )

    def get_user_link ( self ):
        if self.user is None:
            return ""
        try :
            facebook_user = FacebookProfile.objects.get( user = self.user )
            return mark_safe( u'<fb:name uid="%s"  target="_blank" />' % ( facebook_user.uid ) )
        except FacebookProfile.DoesNotExist:
            return mark_safe( self.user.username )

    def __unicode__( self ):
        return self.description

    class Meta:
        verbose_name = _( 'Video' )
        verbose_name_plural = _( 'Videos' )


    def save(self, *args, **kwargs):
        try:
            admin = User.objects.get(username='admin')
            self.user = admin
        except User.DoesNotExsist:
               pass
        super(Video, self).save(*args, **kwargs) # Call the "real" save() method.
