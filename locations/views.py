from django.shortcuts import get_object_or_404
from locations.models import Location, RestaurantType, LocationType, LocationMusic, LocationArea
from django.http import HttpResponseRedirect
from events.models import Event
from django.utils.translation import ugettext as _
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from decorators import render_to
import random
from django.forms import ModelForm
from django.template.defaultfilters import slugify

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
        locations = group.location_set.filter( status = 1 ).all()
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

    slider = Location.objects.filter( status = 1, featured = True ).order_by( '?' )[:3]

    all_locations = Location.objects.all().filter( status = 1 ).order_by( 'title' )

    all_events = Event.objects.all().filter( status = 1 ).order_by( 'title' )


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

from django.contrib.auth.decorators import login_required


@login_required( login_url = '/login/' )
@render_to( 'locations/add.html' )
def add( request ):
    request.breadcrumbs( _( 'Locations' ) , '/locations' )
    request.breadcrumbs( _( 'Add Location' ) , request.path_info )

    class LocationForm( ModelForm ):
        class Meta:
            model = Location
            fields = ( 
                'title',
                'type',
                'restaurant',
                'address',
                'area',
                'city',
                'district',
                'phone_1',
                'phone_2',
                'fax',
                'url',
                'email',
                'days_of_operation',
                'hours_of_operation',
                'music',
                'image_logo',
                'description',

                'owner',
                'contact_type',
                'contact',
                'phones',
                'contact_email',
            )

#LocationForm.visible_fields
            #django.forms.fields.CharField
    if request.method == 'POST': # If the form has been submitted...
        form = LocationForm( request.POST, request.FILES ) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            location = form.save( commit = False )
            location.slug = slugify( location.title )
            #set moderation status
            location.status = 2
            location.save()
            return HttpResponseRedirect( '/locations/' ) # Redirect after POST
        return {
                "form": form,
                "errors": True
        }
    else:
        form = LocationForm()
    return {
        'form': form,
    }
