from decorators import render_to
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.conf import settings
import os, glob, string, re
import shutil

from people.models import PhotoEvent, Photo, PHOTO_CATEGORIES
from django.core.files.base import ContentFile
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext as _

from django.core.paginator import Paginator, InvalidPage, EmptyPage


@render_to( 'people/index.html' )
def index ( request ):
    request.breadcrumbs( _( 'People' ) , '/people' )
    request.breadcrumbs( _( 'By Category' ) , request.path_info )
    groups = []
    for group, description in PHOTO_CATEGORIES:
        events = PhotoEvent.objects.filter( category = group ).order_by( 'datetime_added' )[:5]

        latest_event_photo = events[0]

        groups.append( ( group, description, latest_event_photo, events, ) )

    latest = PhotoEvent.objects.latest( 'datetime_added' )
    return {'groups': groups, 'latest' : latest}

@render_to( 'people/category.html' )
def category ( request, group ):

    events = PhotoEvent.objects.filter( category = group ).order_by( 'datetime_added' )

    if events:
        group_name = events[0].get_category_display()
    else:
        group_name = _( "Empty" )

    request.breadcrumbs( _( 'People' ) , '/people' )
    request.breadcrumbs( group_name , request.path_info )

    try:
        page = int( request.GET.get( 'page', '1' ) )
    except ValueError:
        page = 1

    if events:
        paginator = Paginator( events, 12 )
        try:
            events_page = paginator.page( page )
        except ( EmptyPage, InvalidPage ):
            events_page = paginator.page( paginator.num_pages )

    return {'group_name': group_name, 'current_page': events_page, 'current_paginator': paginator }


@render_to( 'people/slider.html' )
def slider( request , photo_id ):
    photo = get_object_or_404( Photo, pk = photo_id )
    if request.is_ajax():
        return render_to_response( 'people/slider_node.html', {'photo': photo} )

    request.breadcrumbs( _( 'People' ) , '/people' )
    request.breadcrumbs( photo.description , request.path_info )
    return {'photo': photo}


@render_to( 'people/details.html' )
def details ( request, slug ):
    event = get_object_or_404( PhotoEvent, slug = slug )

    request.breadcrumbs( _( 'People' ) , '/people' )
    request.breadcrumbs( event.title , request.path_info )

    try:
        page = int( request.GET.get( 'page', '1' ) )
    except ValueError:
        page = 1

    photos = event.photo_set.all()
    if photos:
        paginator = Paginator( photos, 12 )
        try:
            photos_page = paginator.page( page )
        except ( EmptyPage, InvalidPage ):
            photos_page = paginator.page( paginator.num_pages )

    return {'event': event, 'current_page': photos_page, 'current_paginator': paginator }

@login_required
def make_main ( request, event_id, photo_id ):
    event = get_object_or_404( PhotoEvent, pk = event_id )
    photo = get_object_or_404( Photo, pk = photo_id )
    ft_content = ContentFile( open( photo.image.path, 'r' ).read() )
    event.image.save( photo.image.name, ft_content, save = True )

    return HttpResponseRedirect( '/admin/people/photoevent/%s' % ( event.id ) )


@login_required
@render_to( 'people/select.html' )
def import_select ( request, event_id ):
    event = get_object_or_404( PhotoEvent, pk = event_id )

    dir_list = os.listdir( settings.OLDBOGOTA_PHOTO_PATH )
    return {'dirs': dir_list, 'event': event}

@login_required
def import_finish ( request, event_id, folder ):
    event = get_object_or_404( PhotoEvent, pk = event_id )

    legends_file = settings.OLDBOGOTA_PHOTO_PATH + '/' + folder + '/legends.txt'
    legends = open( legends_file, "r" ).readlines()
    #os.remove( legends_file )

    os.chdir( settings.OLDBOGOTA_PHOTO_PATH + '/' + folder )

    images_list = list()

    def byNumbers( str ):
        g = re.search( r'^(\d+)', str )
        return int( g.group( 1 ) )

    thumb_list = sorted( glob.glob( '*-s.jpg' ) , key = byNumbers )

    for thumb in thumb_list:
        image_file = string.replace( thumb, '-s.jpg', '.jpg' )
        images_list.append( image_file )

    for photo in zip( legends, images_list, thumb_list ) :
        p = Photo( description = photo[0], event = event )

        fi_content = ContentFile( open( settings.OLDBOGOTA_PHOTO_PATH + '/' + folder + '/' + photo[1], 'r' ).read() )
        ft_content = ContentFile( open( settings.OLDBOGOTA_PHOTO_PATH + '/' + folder + '/' + photo[2], 'r' ).read() )

        p.image.save( photo[1], fi_content, save = False )
        p.thumb.save( photo[2], ft_content, save = False )

        p.save()

    shutil.rmtree( settings.OLDBOGOTA_PHOTO_PATH + '/' + folder )

    return HttpResponseRedirect( '/admin/people/photoevent/%s' % ( event.id ) )

