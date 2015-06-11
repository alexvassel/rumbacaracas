from django import template
from django.conf import settings
from django.utils.html import strip_tags
from socialregistration.utils import _https

register = template.Library()

@register.inclusion_tag( 'main/twitter_js.html' )
def twitter_js_tag():
    return {
            'is_https' : bool( _https() )
    }


@register.inclusion_tag( 'main/twitter_share.html' )
def twitter_share( url, text ):
    full_url = settings.FULL_BASE_URL + url
    return dict( url = full_url, text = strip_tags(text) )
