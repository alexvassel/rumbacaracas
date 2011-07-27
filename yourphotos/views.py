from django.shortcuts import render_to_response, get_object_or_404, redirect
from yourphotos.models import Photo
from django.utils.translation import ugettext as _
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from decorators import render_to, json_view
from django.forms import ModelForm
from django.forms.models import modelformset_factory
from django.http import HttpResponseRedirect
from datetime import *;
from dateutil.relativedelta import *

@render_to( 'yourphotos/index.html' )
def photos( request, category ):

    try:
        page = int( request.GET.get( 'page', '1' ) )
    except ValueError:
        page = 1

    request.breadcrumbs( _( 'Your Photos' ) , '/yourphotos' )

    if category == 'latest':
        request.breadcrumbs( _( 'Latest Photos' ) , request.path_info )
        photos = Photo.objects.filter( status = 1 ).order_by( '-datetime_added', '-id' )
    else:
        if category == 'sexy':
            request.breadcrumbs( _( 'Sexy' ) , request.path_info )
        elif category == 'rumbas':
            request.breadcrumbs( _( 'Rumbas' ) , request.path_info )
        elif category == 'amigos':
            request.breadcrumbs( _( 'Amigos' ) , request.path_info )
        elif category == 'humor':
            request.breadcrumbs( _( 'Humor' ) , request.path_info )
        else:
            category = 'sexy'
            request.breadcrumbs( _( 'Sexy' ) , request.path_info )

        photos = Photo.objects.filter( status = 1 ).filter( category = category )

    paginator = Paginator( photos, 12 )
    try:
        photos_page = paginator.page( page )
    except ( EmptyPage, InvalidPage ):
        photos_page = paginator.page( paginator.num_pages )

    latest = Photo.objects.filter( status = 1 ).order_by( '-datetime_added', '-id' )[0]

    return {'latest': latest, 'current_page': photos_page, 'current_paginator': paginator, 'active_tab': category}


@render_to( 'yourphotos/details.html' )
def detail( request , id ):
    photo = get_object_or_404( Photo, pk = id )
    if request.is_ajax():
        return render_to_response( 'yourphotos/details_node.html', {'photo': photo} )
    request.breadcrumbs( _( 'Your Photos' ) , '/yourphotos' )
    request.breadcrumbs( photo.description , request.path_info )
    return {'photo': photo}


@render_to( 'yourphotos/main_ajax_slide.html' )
def main_slide( request , photo_id ):
    if not request.is_ajax():
        return HttpResponseRedirect( '/' )

    photo = get_object_or_404( Photo, pk = photo_id )
    return {'photo': photo}




@json_view
def delete( request , id ):
    add_time = datetime.now() + relativedelta( hours = -6 )
    #delete only my photo, uploaded let's say 6 hours ago maximum
    photo = get_object_or_404( Photo, pk = id, user = request.user, datetime_added__gt = add_time )
    photo.delete()
    return {'success': True}



from django.contrib.auth.decorators import login_required

@login_required( login_url = '/login/' )
@render_to( 'yourphotos/add.html' )
def add( request ):
    request.breadcrumbs( _( 'Your Photos' ) , '/yourphotos' )
    request.breadcrumbs( _( 'Add Photos' ) , request.path_info )

    PhotoFormSet = modelformset_factory( Photo, fields = ( 'image', 'description' ), extra = 5, max_num = 5 )
    if request.method == "POST":
        formset = PhotoFormSet( request.POST, request.FILES,
                                queryset = Photo.objects.none() )
        if formset.is_valid():
            photos = formset.save( commit = False )
            for photo in photos:
                photo.user = request.user
                photo.save()

            formset = PhotoFormSet( queryset = Photo.objects.none() )
            #return HttpResponseRedirect( "/yourphotos" )
            return {
                    "formsets": formset,
                    "completed": True,
                    "photos": photos
            }

            # Do something.
        return {
                "formsets": formset,
                "errors": True
        }
    else:
        formset = PhotoFormSet( queryset = Photo.objects.none() )
    return {
        "formsets": formset,
    }
