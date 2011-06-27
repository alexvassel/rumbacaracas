from django_openx import Zone
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def get_tag_for_zone( zone_id ):
    try:
        zone_id = int( zone_id )
        zone = Zone.get( zone_id )
        return mark_safe( zone.generate_tag() )
    except:
        return "" # Fail silently.

get_tag_for_zone.is_safe = True




class ZoneNode( template.Node ):
    def __init__( self, zone_id, type ):
        self.zone_id = zone_id
        self.type = type

    def render( self, context ):
        try:
            zone = Zone.get( self.zone_id )
            return mark_safe( zone.generate_tag( code_type = self.type ) )
        except Exception, e:
            return "" # Fail silently.


@register.tag( name = "banner_zone" )
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

