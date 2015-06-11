from django.template.defaultfilters import stringfilter
from django import template
import re
from django.utils.safestring import mark_safe

register = template.Library()



@register.inclusion_tag('main/youtube_video.html')
def youtube_video( youtube_id, width = 600 , height=390 ):
    return dict( youtube_id = youtube_id, width = width, height = height )





@register.filter
def youtube_video_from_id( video_id ):
    #return """
    #<object width="425" height="344">
    #<param name="movie" value="http://www.youtube.com/watch/v/%s"></param>
    #<param name="allowFullScreen" value="true"></param>
    #<embed src="http://www.youtube.com/watch/v/%s" type="application/x-shockwave-flash" allowfullscreen="true" width="425" height="344"></embed>
    #</object>
    #""" % ( video_id, video_id )

    video = '''<object width="600" height="390">
      <param name="movie" value="http://www.youtube.com/v/%s"/>
      <param name="wmode" value="transparent"/>
      <embed src="http://www.youtube.com/v/%s" type="application/x-shockwave-flash" wmode="transparent" width="600" height="390"/>
    </object>''' % ( video_id, video_id )

    return mark_safe( video )
youtube_video_from_id.is_safe = True # Don't escape HTML

@register.filter
@stringfilter
def youtube( url ):
    regex = re.compile( r"^(http://)?(www\.)?(youtube\.com/watch\?v=)?(?P<id>[A-Za-z0-9\-=_]{11})" )
    match = regex.match( url )
    if not match: return ""
    video_id = match.group( 'id' )
    return youtube_video_from_id( video_id )
youtube.is_safe = True # Don't escape HTML


@register.filter
@stringfilter
def youtube_img_from_id( video_id ):
    return "http://img.youtube.com/vi/%s/2.jpg" % ( video_id, )
youtube_img_from_id.is_safe = True # Don't escape HTML

@register.filter
@stringfilter
def youtube_img( url ):
    regex = re.compile( r"^(http://)?(www\.)?(youtube\.com/watch\?v=)?(?P<id>[A-Za-z0-9\-=_]{11})" )
    match = regex.match( url )
    if not match: return ""
    video_id = match.group( 'id' )
    return youtube_img_from_id( video_id )

