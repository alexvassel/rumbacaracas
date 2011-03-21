from django.shortcuts import render_to_response, get_object_or_404
from locations.models import Location, RestaurantType, LocationType, LocationMusic, LocationArea
from django.utils.translation import ugettext as _
from django.template import RequestContext

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


@render_to( 'locations/index.html' )
def category( request ):
    request.breadcrumbs( _( 'Locations' ) , '/locations' )
    request.breadcrumbs( _( 'By category' ) , request.path_info )

    group_field = LocationType.objects.select_related().all()
    all_locations = Location.objects.all()
    return {'all_locations': all_locations, 'group_field': group_field, 'view': 'category'}

def category_detail( request ):
    pass

@render_to( 'locations/index.html' )
def area( request ):
    request.breadcrumbs( _( 'Locations' ) , '/locations' )
    request.breadcrumbs( _( 'By area' ) , request.path_info )
    group_field = LocationArea.objects.select_related().all()
    all_locations = Location.objects.all()
    return {'all_locations': all_locations, 'group_field': group_field, 'view': 'area'}

def area_detail( request ):
    pass

@render_to( 'locations/index.html' )
def music( request ):
    request.breadcrumbs( _( 'Locations' ) , '/locations' )
    request.breadcrumbs( _( 'By music' ) , request.path_info )
    group_field = LocationMusic.objects.select_related().all()
    all_locations = Location.objects.all()
    return {'all_locations': all_locations, 'group_field': group_field, 'view': 'music'}

def music_detail( request ):
    pass

@render_to( 'locations/index.html' )
def food( request ):
    request.breadcrumbs( _( 'Locations' ) , '/locations' )
    request.breadcrumbs( _( 'By type of food' ) , request.path_info )
    group_field = RestaurantType.objects.select_related().all()
    all_locations = Location.objects.all()
    return {'all_locations': all_locations, 'group_field': group_field, 'view': 'food'}

def food_detail( request ):
    pass

@render_to( 'locations/detail.html' )
def detail ( request, slug ):
    location = get_object_or_404( Location, slug = slug )
    request.breadcrumbs( _( 'Locals' ) , '/locations' )
    request.breadcrumbs( location.title , request.path_info )
    return {'location': location}
