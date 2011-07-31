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
from django.forms import forms
from people.models import PhotoEvent
from datetime import datetime, timedelta, time
from main.modelFields import SlugifyUniquely

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


@render_to( 'locations/category.html' )
def category_details ( request, group ):

    locations = Location.objects.filter( status = 1 ).filter( type__slug = group ).order_by( 'title' )

    group_name = LocationType.objects.get(slug=group)
    
    request.breadcrumbs( _( 'Locations' ) , '/locations' )
    request.breadcrumbs( group_name , request.path_info )

    try:
        page = int( request.GET.get( 'page', '1' ) )
    except ValueError:
        page = 1

    if locations:
        paginator = Paginator( locations, 12 )
        try:
            locations_page = paginator.page( page )
        except ( EmptyPage, InvalidPage ):
            locations_page = paginator.page( paginator.num_pages )
    else:
        locations_page = None
        paginator = None
    return {'group_name': group_name, 'current_page': locations_page, 'current_paginator': paginator }



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

    today = datetime.today().date()
    
    location_events_raw = Event.objects.filter(status=1, location=location)[:5]
    
    #TODO wrong check if upcoming
    location_events = [((event.from_date >= today), event) for event in location_events_raw ]
    location_photos = PhotoEvent.objects.filter(status=1, location=location).order_by('-datetime_added')[:5]
    
    request.breadcrumbs( _( 'Locations' ) , '/locations' )
    request.breadcrumbs( location.title , request.path_info )
    dict = _process( request, LocationType )
    dict['location'] = location
    dict['active_tab'] = 'category'
    dict['location_events'] = location_events
    dict['location_photos'] = location_photos
    return dict

from django.contrib.auth.decorators import login_required


@login_required( login_url = '/login/' )
@render_to( 'locations/add.html' )
def add( request ):
    request.breadcrumbs( _( 'Locations' ) , '/locations' )
    request.breadcrumbs( _( 'Add Location' ) , request.path_info )

    class LocationForm( ModelForm ):
        #type = ModelMultipleChoiceField( queryset = LocationType.objects.all() )

        class Meta:
            model = Location
            fields = ( 
                'title',
                'type',
                'restaurant',
                'address',
                'area',
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
        #Set required
        def clean_type(self):
            type = self.cleaned_data.get("type")
            if not type:
                raise forms.ValidationError( _("This field is required"))
            return type

        #Set required
        def clean_address(self):
            address = self.cleaned_data.get("address")
            if not address:
                raise forms.ValidationError( _("This field is required"))
            return address
        #Set required
        def clean_area(self):
            area = self.cleaned_data.get("area")
            if not area:
                raise forms.ValidationError( _("This field is required"))
            return area
        #Set required
        def clean_days_of_operation(self):
            days_of_operation = self.cleaned_data.get("days_of_operation")
            if not days_of_operation:
                raise forms.ValidationError( _("This field is required"))
            return days_of_operation
        #Set required
        def clean_hours_of_operation(self):
            hours_of_operation = self.cleaned_data.get("hours_of_operation")
            if not hours_of_operation:
                raise forms.ValidationError( _("This field is required"))
            return hours_of_operation
        #Set required
        def clean_music(self):
            music = self.cleaned_data.get("music")
            if not music:
                raise forms.ValidationError( _("This music is required"))
            return music
        #Set required
        def clean_image_logo(self):
            image_logo = self.cleaned_data.get("image_logo")
            if not image_logo:
                raise forms.ValidationError( _("This field is required"))
            return image_logo
        #Set required
        def clean_description(self):
            description = self.cleaned_data.get("description")
            if not description:
                raise forms.ValidationError( _("This field is required"))
            return description

        #Set required type of restaurant if type is restaurant
        def clean(self):
            cleaned_data = self.cleaned_data

            type = cleaned_data.get("type")
            restaurant = cleaned_data.get("restaurant")

            if not type:
                return cleaned_data
            #TODO Remove Magic number
            elif 11 in [typ.pk for typ in type]:
                if not restaurant:
                    raise forms.ValidationError( _("Type of restaurant can't be empty for restaurant"))
                
            return cleaned_data

#LocationForm.visible_fields
            #django.forms.fields.CharField
    if request.method == 'POST': # If the form has been submitted...
        form = LocationForm( request.POST, request.FILES ) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            location = form.save( commit = False )
            location.slug = SlugifyUniquely(location.title, location.__class__)
            #set moderation status
            location.status = 2
            location.add_user = request.user
            location.save()
            form.save_m2m()
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
