from django_openx import Zone
from django import template
from django.utils.safestring import mark_safe
from socialregistration.utils import _https
from decorators import cache

register = template.Library()

@register.inclusion_tag( 'main/openx_spc_js.html' )
def openxspc_js_tag():
    return {
            'is_https' : bool( _https() )
    }




@cache(600)
def get_tag_for_zone_raw (zone_id):
    # ALARM ALARM
    #return ""

    zone = Zone.get( zone_id )

    tag = zone.generate_tag(code_type='adjs')
    return tag


@register.filter
def get_tag_for_zone( zone_id ):
    try:
        zone_id = int( zone_id )
        return mark_safe( get_tag_for_zone_raw(zone_id) )
    except:
        return "" # Fail silently.

get_tag_for_zone.is_safe = True




class ZoneNode( template.Node ):
    def __init__( self, zone_id, type ):
        self.zone_id = zone_id
        self.type = type

    def render( self, context ):
        try:
            return mark_safe( get_tag_for_zone_raw(self.zone_id) )
        except Exception, e:
            return "" # Fail silently.

#register.tag( name = "banner_zone" )
def embed_zone_tag( parser, token ):

    bits = token.contents.split()

    if len( bits ) not in [2, 3]:
        raise template.TemplateSyntaxError, "tag takes two or three arguments"

    if len( bits ) == 3:
        zone_id = int( bits[1] )
        type = bits[2]
    else:
        zone_id = int( bits[1] )
        type = 'adjs'

    return ZoneNode( zone_id, type )


#Simplest iframe integration
@register.inclusion_tag( 'main/openx_banner.html' )
def banner_zone_iframe( zone_id, width=None, height=None ):
    return dict( zone_id = zone_id, width = width, height=height )
