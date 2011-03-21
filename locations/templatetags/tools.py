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


def paginator( context, adjacent_pages = 2 ):
    """
    To be used in conjunction with the object_list generic view.

    Adds pagination context variables for use in displaying first, adjacent and
    last page links in addition to those created by the object_list generic
    view.

    """
    table = context['table']
    startPage = max( table.page.number - adjacent_pages, 1 )
    if startPage <= 3: startPage = 1
    endPage = table.page.number + adjacent_pages + 1
    if endPage >= table.paginator.num_pages - 1: endPage = table.paginator.num_pages + 1
    page_numbers = [n for n in range( startPage, endPage ) \
            if n > 0 and n <= table.paginator.num_pages]
    page_obj = table.paginator.page
    paginator = table.paginator

    return {
        'page_obj': page_obj,
        'paginator': paginator,
        'page': table.page.number,
        'pages': table.paginator.num_pages ,
        'page_numbers': page_numbers,
        'next': table.page.next_page_number(),
        'previous': table.page.previous_page_number() ,
        'has_next': table.page.has_next(),
        'has_previous': table.page.has_previous(),
        'show_first': 1 not in page_numbers,
        'query': table.query,
        'sort': table.sort,
        'show_last': table.paginator.num_pages  not in page_numbers,
    }

register.inclusion_tag( 'paginator.html', takes_context = True )( paginator )
