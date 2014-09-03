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


import random


#Simplest iframe integration
@register.inclusion_tag( 'main/openx_banner.html' )
def banner_zone_iframe( zone_id, width=None, height=None, noupdate=None ):
    rand = int(100000 * random.random())
    if noupdate != None:
        noupdate = 1
    else:
        noupdate = 0
    return dict( zone_id = zone_id, width = width, height=height,rand =rand, noupdate = noupdate  )

#Simplest iframe integration
@register.inclusion_tag( 'main/openx_banner_updated.html' )
def banner_zone_iframe_updated( zone_id, width=None, height=None, noupdate=None ):
    rand = int(100000 * random.random())
    if noupdate != None:
        noupdate = 1
    else:
        noupdate = 0
    return dict( zone_id = zone_id, width = width, height=height,rand =rand, noupdate = noupdate  )


@register.inclusion_tag( 'main/revive_banner.html' )
def revive_banner( zone_id, width=None, height=None, n=None, noupdate=None ):
    rand = int(100000 * random.random())
    if noupdate != None:
        noupdate = 1
    else:
        noupdate = 0
    return dict( zone_id = zone_id, width = width, height=height,rand =rand, n=n, noupdate = noupdate  )


#@register.inclusion_tag( 'main/openx_float_banner.html' )
#def banner_zone_float( zone_id, width=None, height=None ):
#    rand = round(100000 * random.random(), 5)
#    return dict( zone_id = zone_id, width = width, height=height,rand =rand  )

#@register.inclusion_tag( 'main/openx_overflow_banner.html' )
#def banner_zone_overflow( zone_id, width=None, height=None ):
#    rand = round(100000 * random.random(), 5)
#    return dict( zone_id = zone_id, width = width, height=height,rand =rand  )

@register.inclusion_tag( 'main/revive_float_banner.html' )
def banner_revive_float( zone_id, width=None, height=None, n=None ):
    rand = round(100000 * random.random(), 5)
    return dict( zone_id = zone_id, width = width, height=height, rand=rand, n=n  )

#this function will be removed later since we have replaced openx with latest version. i.e. revive.
@register.inclusion_tag( 'main/openx_corner_banner.html' )
def banner_zone_corner( zone_id, width=None, height=None, n=None ):
    rand = round(100000 * random.random(), 5)
    return dict( zone_id = zone_id, width = width, height=height,rand =rand, n=n  )

@register.inclusion_tag( 'main/revive_corner_banner.html' )
def revive_zone_corner( zone_id, width=None, height=None, n=None ):
    rand = round(100000 * random.random(), 5)
    return dict( zone_id = zone_id, width = width, height=height,rand =rand, n=n  )


@register.inclusion_tag( 'main/openx_email_banner.html' )
def banner_zone_email( zone_id):
    rand = random.random()
    return dict( zone_id = zone_id, rand = rand  )

@register.inclusion_tag( 'main/openx_overlay_banner.html' )
def overlay_banner( zone_id):
    rand = random.random()
    return dict( zone_id = zone_id, rand = rand  )

