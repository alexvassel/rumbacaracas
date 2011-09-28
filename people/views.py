from decorators import render_to
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.conf import settings
from django.core.files.storage import default_storage
import os, glob, string, re
import shutil

from people.models import PhotoEvent, Photo, PHOTO_CATEGORIES
from django.core.files.base import ContentFile
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext as _

from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse

@render_to( 'people/index.html' )
def index ( request ):
    request.breadcrumbs( _( 'People' ) , reverse('people_main') )
    request.breadcrumbs( _( 'By Category' ) , request.path_info )
    groups = []
    for group, description in PHOTO_CATEGORIES:
        events = PhotoEvent.objects.filter( status = 1 ).filter( category = group ).order_by( '-date' )[:5]
        if events:
            latest_event_photo = events[0]
            groups.append( ( group, description, latest_event_photo, events, ) )

    latest = PhotoEvent.objects.filter( status = 1 ).latest( 'date' )
    return {'groups': groups, 'latest' : latest}

@render_to( 'people/category.html' )
def category ( request, group ):

    events = PhotoEvent.objects.filter( status = 1 ).filter( category = group ).order_by( 'date' )

    if events:
        group_name = events[0].get_category_display()
    else:
        group_name = _( "Empty" )

    request.breadcrumbs( _( 'People' ) , reverse('people_main') )
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

    request.breadcrumbs( _( 'People' ) , reverse('people_main') )
    request.breadcrumbs( photo.event.title , request.path_info )
    return {'photo': photo}


@render_to( 'people/main_ajax_slide.html' )
def main_slide( request , event_id ):
    if not request.is_ajax():
        return HttpResponseRedirect( '/' )
    
    event = get_object_or_404( PhotoEvent, pk = event_id )
    return {'event': event}



@render_to( 'people/details.html' )
def details ( request, slug ):
    event = get_object_or_404( PhotoEvent, slug = slug, status = 1 )

    request.breadcrumbs( _( 'People' ) , reverse('people_main') )
    request.breadcrumbs( event.title , request.path_info )

    try:
        page = int( request.GET.get( 'page', '1' ) )
    except ValueError:
        page = 1

    photos = event.photo_set.all().order_by('datetime_added', 'id')
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
    ft_content = ContentFile( photo.image.file.read() )
    event.image.save( photo.image.name, ft_content, save = True )

    return HttpResponseRedirect( '/admin/people/photoevent/%s' % ( event.id ) )


@login_required
@render_to( 'people/select.html' )
def import_select ( request, event_id ):
    event = get_object_or_404( PhotoEvent, pk = event_id )

    dir_list = os.listdir( settings.OLDCARACAS_PHOTO_PATH )
    return {'dirs': dir_list, 'event': event}

@login_required
def import_finish ( request, event_id, folder ):
    event = get_object_or_404( PhotoEvent, pk = event_id )

    legends_file = settings.OLDCARACAS_PHOTO_PATH + '/' + folder + '/legends.txt'
    legends = open( legends_file, "r" ).readlines()
    #os.remove( legends_file )

    os.chdir( settings.OLDCARACAS_PHOTO_PATH + '/' + folder )

    images_list = list()

    def byNumbers( str ):
        g = re.search( r'^(\d+)', str )
        return int( g.group( 1 ) )

    thumb_list = sorted( glob.glob( '*-s.jpg' ) , key = byNumbers )

    for thumb in thumb_list:
        image_file = string.replace( thumb, '-s.jpg', '.jpg' )
        images_list.append( image_file )


    import Queue
    import threading
    class ThreadProcessPage( threading.Thread ):
        """Threaded photo copy"""
        def __init__( self, queue ):
            threading.Thread.__init__( self )
            self.queue = queue

        def run( self ):
            while True:
                photo = self.queue.get()
                try:
                    udescription = unicode(photo[0], "latin-1")
                    p = Photo( description = udescription, event = event )
                    fi_content = ContentFile( open( settings.OLDCARACAS_PHOTO_PATH + '/' + folder + '/' + photo[1], 'r' ).read() )
                    ft_content = ContentFile( open( settings.OLDCARACAS_PHOTO_PATH + '/' + folder + '/' + photo[2], 'r' ).read() )
                    p.image.save( photo[1], fi_content, save = False )
                    p.thumb.save( photo[2], ft_content, save = False )
                    p.save()

                except:
                    pass
                self.queue.task_done()

    queue = Queue.Queue()
    threadLock = threading.Lock()
    #spawn a pool of threads, and pass them queue instance
    for i in range( 5 ):
        t = ThreadProcessPage( queue )
        t.setDaemon( True )
        t.start()

    for photo in zip( legends, images_list, thumb_list ) :
        queue.put( photo )

    queue.join()

    shutil.rmtree( settings.OLDCARACAS_PHOTO_PATH + '/' + folder )

    return HttpResponseRedirect( '/admin/people/photoevent/%s' % ( event.id ) )

