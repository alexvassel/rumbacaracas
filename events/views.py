from django.shortcuts import get_object_or_404
from events.models import EventCategory, Event, WeekDay
from django.utils.translation import ugettext as _
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from decorators import render_to

def _process( request, group ):
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
