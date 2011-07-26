from django import template
from django.conf import settings

register = template.Library()

@register.inclusion_tag( 'main/gplus_js.html' )
def gplus_js_tag():
    return {}


@register.inclusion_tag( 'main/gplus.html' )
def gplus( url):
    full_url = settings.FULL_BASE_URL + url
    return dict( url = full_url)

