from django.shortcuts import render_to_response, get_object_or_404
from locations.models import Location, RestaurantType, LocationType, LocationMusic, LocationArea
from django.utils.translation import ugettext as _
from django.template import RequestContext
from django.core.paginator import Paginator, InvalidPage, EmptyPage

def render_response( req, *args, **kwargs ):
    kwargs['context_instance'] = RequestContext( req )
    return render_to_response( *args, **kwargs )


def render_to( tmpl ):
    """
    Decorator for Django views that sends returned dict to render_to_response function
    with given template and RequestContext as context instance.

    If view doesn't return dict then decorator simply returns output.
    """
    def renderer( func ):
        def wrapper( request, *args, **kw ):
            output = func( request, *args, **kw )
            if not isinstance( output, dict ):
                return output
            return render_response( request, tmpl, output )
        return wrapper
    return renderer


def _process( request, group ):
    try:
        page = int( request.GET.get( 'page', '1' ) )
    except ValueError:
        page = 1

    try:
        group_id = int( request.GET.get( 'group_id', 0 ) )
    except ValueError:
        group_id = 0

    group_fields = group.objects.select_related().all()
    groups = []
    counter = 0
    for group in group_fields:
        locations = group.location_set.all()
        if locations:
            paginator = Paginator( locations, 6 )
            try:
                if ( counter == group_id ):
                    locations_page = paginator.page( page )
                else:
                    locations_page = paginator.page( 1 )
            except ( EmptyPage, InvalidPage ):
                locations_page = paginator.page( paginator.num_pages )
            groups.append( ( group.title , locations_page, paginator ) )
            counter = counter + 1

    all_locations = Location.objects.all()
    return {'all_locations': all_locations, 'groups': groups, 'active_group' : group_id}


@render_to( 'locations/index.html' )
def category( request ):
    request.breadcrumbs( _( 'Locations' ) , '/locations' )
    request.breadcrumbs( _( 'By category' ) , request.path_info )
    dict = _process( request, LocationType )
    dict['active_tab'] = 'category'
    return dict


@render_to( 'locations/index.html' )
def area( request ):
    request.breadcrumbs( _( 'Locations' ) , '/locations' )
    request.breadcrumbs( _( 'By area' ) , request.path_info )
    dict = _process( request, LocationArea )
    dict['active_tab'] = 'area'
    return dict


@render_to( 'locations/index.html' )
def music( request ):
    request.breadcrumbs( _( 'Locations' ) , '/locations' )
    request.breadcrumbs( _( 'By music' ) , request.path_info )
    dict = _process( request, LocationMusic )
    dict['active_tab'] = 'music'
    return dict

@render_to( 'locations/index.html' )
def food( request ):
    request.breadcrumbs( _( 'Locations' ) , '/locations' )
    request.breadcrumbs( _( 'By type of food' ) , request.path_info )
    dict = _process( request, RestaurantType )
    dict['active_tab'] = 'food'
    return dict

@render_to( 'locations/index.html' )
def detail ( request, slug ):
    location = get_object_or_404( Location, slug = slug )
    request.breadcrumbs( _( 'Locations' ) , '/locations' )
    request.breadcrumbs( location.title , request.path_info )
    dict = _process( request, LocationType )
    dict['location'] = location
    dict['active_tab'] = 'category'
    return dict
