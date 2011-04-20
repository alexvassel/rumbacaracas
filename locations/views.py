from django.shortcuts import get_object_or_404
from locations.models import Location, RestaurantType, LocationType, LocationMusic, LocationArea

from events.models import Event

from django.utils.translation import ugettext as _
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from decorators import render_to
import random

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

    slider = Location.objects.order_by( '?' )[:3]

    all_locations = Location.objects.all().order_by( 'title' )

    all_events = Event.objects.all().order_by( 'title' )


    return {'all_locations': all_locations, 'groups': groups, 'active_group' : group_id, 'slider': slider, 'all_events': all_events}


@render_to( 'locations/index.html' )
def category( request ):
    request.breadcrumbs( _( 'Locations' ) , '/locations' )
    request.breadcrumbs( _( 'By Category' ) , request.path_info )
    dict = _process( request, LocationType )
    dict['active_tab'] = 'category'
    return dict


@render_to( 'locations/index.html' )
def area( request ):
    request.breadcrumbs( _( 'Locations' ) , '/locations' )
    request.breadcrumbs( _( 'By Area' ) , request.path_info )
    dict = _process( request, LocationArea )
    dict['active_tab'] = 'area'
    return dict


@render_to( 'locations/index.html' )
def music( request ):
    request.breadcrumbs( _( 'Locations' ) , '/locations' )
    request.breadcrumbs( _( 'By Music' ) , request.path_info )
    dict = _process( request, LocationMusic )
    dict['active_tab'] = 'music'
    return dict

@render_to( 'locations/index.html' )
def food( request ):
    request.breadcrumbs( _( 'Locations' ) , '/locations' )
    request.breadcrumbs( _( 'By Type of Food' ) , request.path_info )
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
