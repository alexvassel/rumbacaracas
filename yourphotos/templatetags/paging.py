from django import template
register = template.Library()


def common_paginator( context, adjacent_pages = 2, anchor = None ):

    current_page = context['current_page']
    current_paginator = context['current_paginator']
    startPage = max( current_page.number - adjacent_pages, 1 )
    if startPage <= 3: startPage = 1
    endPage = current_page.number + adjacent_pages + 1
    if endPage >= current_paginator.num_pages - 1: endPage = current_paginator.num_pages + 1
    page_numbers = [n for n in range( startPage, endPage ) \
            if n > 0 and n <= current_paginator.num_pages]
    page_obj = current_paginator.page
    paginator = current_paginator
    return {
        'page_obj': page_obj,
        'paginator': paginator,
        'page': current_page.number,
        'pages': current_paginator.num_pages ,
        'page_numbers': page_numbers,
        'next': current_page.next_page_number(),
        'previous': current_page.previous_page_number() ,
        'has_next': current_page.has_next(),
        'has_previous': current_page.has_previous(),
        'show_first': 1 not in page_numbers,
        'show_last': current_paginator.num_pages  not in page_numbers,
        'anchor': anchor
    }

register.inclusion_tag( 'common_paginator.html', takes_context = True )( common_paginator )


