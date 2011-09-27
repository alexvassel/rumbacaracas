from django import template
from django.template import TemplateSyntaxError
from django.template.defaultfilters import urlencode
from socialregistration.models import FacebookProfile, TwitterProfile
register = template.Library()
from django.utils.safestring import mark_safe
from locations.models import LocationType, Location
from events.models import Event
from django.utils.html import strip_tags
from django.conf import settings
from django.core.urlresolvers import reverse

@register.filter
def truncate( value, arg ):
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
        from django.utils.html import escape
        return mark_safe( '<span title="' + escape(strip_tags(value))[:200] + '">' + strip_tags(value)[:length] + "..." + '</span>' )
    else:
        return value


@register.filter
def get_event_url_by_tab( value, arg):
    """
    Get event url according to input category and arg as period
    """
    try:
        tab = str( value )
        period = str( arg )
    except ValueError: # invalid literal for int()
        return value # Fail silently.
    if tab == 'calendar':
        tab = 'category'
    return reverse('event_by_'+ tab + '_' + period )


@register.filter
def user_link( value ):
    if value is None or value == "":
        return ""
    try :
        facebook_user = FacebookProfile.objects.get( user = value )
    except FacebookProfile.DoesNotExist:
        facebook_user = None

    try :
        twitter_user = TwitterProfile.objects.get( user = value )
    except TwitterProfile.DoesNotExist:
        twitter_user = None

    if facebook_user is not None:
        return mark_safe( u'<fb:name uid="%s"  target="_blank" />' % ( facebook_user.uid ) )
    elif twitter_user is not None:
        return mark_safe( value.username )
    #elif value.first_name or value.last_name:
        #return mark_safe( '%s %s' % (value.first_name, value.last_name))
    else:
        return mark_safe( value.username )


@register.filter
def google_map_link( value):

    if value is None:
        return ""
    
    query = list()
    if isinstance(value, Location):
        if value.address:
            query.append(value.address)

        if value.city:
            query.append(value.city)

    elif isinstance(value, Event):
        if value.location:
            if value.location.address:
                query.append(value.location.address)

            if value.location.city:
                query.append(value.location.city)
        else:
            if value.address:
                query.append(value.address)

            if value.city:
                query.append(value.city)
    else:
        return ""

    query.append("Colombia")

    return 'http://map.google.es/maps?q=%s' % (urlencode(" ".join(query)))


@register.inclusion_tag( 'main/location_menu.html' )
def show_location_menu( ):
    categories = LocationType.objects.filter(show_in_menu=True).order_by( 'title' )
    return dict( categories = categories)



def locations_paginator( context, adjacent_pages = 2 ):
    """
    To be used in conjunction with the object_list generic view.

    Adds pagination context variables for use in displaying first, adjacent and
    last page links in addition to those created by the object_list generic
    view.

    """

    group_num = context['forloop']['counter0']
    locations_page = context['locations_page']
    locations_paginator = context['locations_paginator']
    startPage = max( locations_page.number - adjacent_pages, 1 )
    if startPage <= 3: startPage = 1
    endPage = locations_page.number + adjacent_pages + 1
    if endPage >= locations_paginator.num_pages - 1: endPage = locations_paginator.num_pages + 1
    page_numbers = [n for n in range( startPage, endPage ) \
            if n > 0 and n <= locations_paginator.num_pages]
    page_obj = locations_paginator.page
    paginator = locations_paginator
    return {
        'page_obj': page_obj,
        'group_num': group_num,
        'paginator': paginator,
        'page': locations_page.number,
        'pages': locations_paginator.num_pages ,
        'page_numbers': page_numbers,
        'next': locations_page.next_page_number(),
        'previous': locations_page.previous_page_number() ,
        'has_next': locations_page.has_next(),
        'has_previous': locations_page.has_previous(),
        'show_first': 1 not in page_numbers,
        'show_last': locations_paginator.num_pages  not in page_numbers,
    }

register.inclusion_tag( 'paginator.html', takes_context = True )( locations_paginator )



def zinnie_paginator( context, adjacent_pages = 2, anchor = None ):

    page_numbers = [n for n in \
                    range(context['page'] - adjacent_pages, context['page'] + adjacent_pages + 1) \
                    if n > 0 and n <= context['pages']]
    return {
        'hits': context['hits'],
        'results_per_page': context['results_per_page'],
        'page': context['page'],
        'pages': context['pages'],
        'page_numbers': page_numbers,
        'next': context['next'],
        'previous': context['previous'],
        'has_next': context['has_next'],
        'has_previous': context['has_previous'],
        'show_first': 1 not in page_numbers,
        'show_last': context['pages'] not in page_numbers,
        'anchor': anchor
    }

register.inclusion_tag( 'common_paginator.html', takes_context = True )( zinnie_paginator )



@register.filter
def hash( h, key ):
    try:
        return h[key]
    except KeyError: # invalid literal for int()
        return '' # Fail silently.




import random
@register.filter
def randomv(value):
    if not value:
        value = 0.5
    if random.random() <= value:
        return True
    else:
        return False



@register.tag
def value_from_settings(parser, token):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, var = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires a single argument" % token.contents.split()[0]
    if not (var[0] == var[-1] and var[0] in ('"', "'")):
        raise template.TemplateSyntaxError("%r tag's argument should be in quotes" % tag_name)
    return ValueFromSettings(var[1:-1])

class ValueFromSettings(template.Node):
    def __init__(self, var):
        self.arg = template.Variable(var)
    def render(self, context):
        return settings.__getattr__(str(self.arg))


@register.inclusion_tag( 'events/group_block.html' )
def show_event_group( events, period, closest_dates ):
    events_thums = list()
    events_list = list()
    
    if len(events) > 10:
        events_thums = events[0:8]
        events_list = events[8:]
    else:
        events_thums = events
    return dict( events_list = events_list,events_thums = events_thums, period = period, closest_dates = closest_dates  )