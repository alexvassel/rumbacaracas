from decorators import render_to
from django.http import HttpResponseRedirect
from django.conf import settings
import os, glob, string, re
import shutil

from peoples.models import PhotoEvent, Photo
from django.shortcuts import get_object_or_404
from django.core.files.base import ContentFile
from django.contrib.auth.decorators import login_required

@login_required
@render_to( 'peoples/select.html' )
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

    return HttpResponseRedirect( '/admin/peoples/photoevent/%s' % ( event.id ) )

