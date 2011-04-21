from django import template
register = template.Library()

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
    if ( len( value ) > length ):
        from django.utils.safestring import mark_safe
        return mark_safe( '<span title="' + value + '">' + value[:length] + "..." + '</span>' )
    else:
        return value


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


@register.filter
def hash( h, key ):
    try:
        return h[key]
    except KeyError: # invalid literal for int()
        return '' # Fail silently.

