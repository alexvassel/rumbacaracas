from django import template
from django.conf import settings
from socialregistration.utils import _https
from django.utils.html import strip_tags

register = template.Library()

@register.inclusion_tag( 'main/facebook_js.html' )
def facebook_js_tag():
    return {
            'facebook_api_key' : settings.FACEBOOK_API_KEY,
            'is_https' : bool( _https() )
    }


@register.inclusion_tag( 'main/facebook_comments.html' )
def facebook_comments( url ):
    full_url = settings.FULL_BASE_URL + url
    return dict( url = full_url )


@register.inclusion_tag( 'main/facebook_like.html' )
def facebook_like( url, width = 90 , send = True ):
    full_url = settings.FULL_BASE_URL + url
    return dict( url = full_url, width = width, send = send )



@register.inclusion_tag( 'main/facebook_send.html' )
def facebook_send( url ):
    full_url = settings.FULL_BASE_URL + url
    return dict( url = full_url )



@register.inclusion_tag( 'main/facebook_comments_count.html' )
def facebook_comments_count( url ):
    full_url = settings.FULL_BASE_URL + url
    return dict( url = full_url )



@register.inclusion_tag( 'main/facebook_group.html' )
def facebook_group():
    return dict( url = settings.FULL_BASE_URL )



@register.filter
def truncate_raw( value, arg ):
    """
    Truncates a string after a given number of chars
    return abbr with title
    Argument: Number of chars to truncate after
    """
    try:
        length = int( arg )
    except ValueError: # invalid literal for int()
        return value # Fail silently.
    if not isinstance( value, basestring ):
        value = str( value )
    if ( len( strip_tags(value) ) > length ):
        from django.utils.safestring import mark_safe
        return mark_safe( strip_tags(value)[:length] + "..." )
    else:
        return value



