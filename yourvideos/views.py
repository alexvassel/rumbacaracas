from django.shortcuts import render_to_response, get_object_or_404, redirect
from yourvideos.models import  Video
from django.utils.translation import ugettext as _
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from decorators import render_to, json_view
from django.forms import ModelForm
from django.forms.models import modelformset_factory
from django.http import HttpResponseRedirect
from datetime import *;
from dateutil.relativedelta import *

@render_to( 'yourvideos/index.html' )
def index( request ):

    try:
        page = int( request.GET.get( 'page', '1' ) )
    except ValueError:
        page = 1

    request.breadcrumbs( _( 'Your Videos' ) , '/videos' )

    videos = Video.objects.filter( status = 1 ).order_by( '-datetime_added' )


    paginator = Paginator( videos, 12 )
    try:
        videos_page = paginator.page( page )
    except ( EmptyPage, InvalidPage ):
        videos_page = paginator.page( paginator.num_pages )

    latest = Video.objects.filter( status = 1 ).latest( 'datetime_added' )

    return {'latest': latest, 'current_page': videos_page, 'current_paginator': paginator}


@render_to( 'yourvideos/details.html' )
def detail( request , id ):
    video = get_object_or_404( Video, pk = id )
    request.breadcrumbs( _( 'Your Videos' ) , '/videos' )
    request.breadcrumbs( video.description , request.path_info )
    return {'video': video}

@json_view
def delete( request , id ):
    add_time = datetime.now() + relativedelta( hours = -6 )
    #delete only my photo, uploaded let's say 6 hours ago maximum
    video = get_object_or_404( Video, pk = id, user = request.user, datetime_added__gt = add_time )
    video.delete()
    return {'success': True}



from django.contrib.auth.decorators import login_required

@login_required( login_url = '/login/' )
@render_to( 'yourvideos/add.html' )
def add( request ):
    request.breadcrumbs( _( 'Your Videos' ) , '/videos' )
    request.breadcrumbs( _( 'Add Video' ) , request.path_info )

    VideoFormSet = modelformset_factory( Video, fields = ( 'youtube_id', 'description' ), extra = 5, max_num = 5 )
    if request.method == "POST":
        formset = VideoFormSet( request.POST, request.FILES,
                                queryset = Video.objects.none() )
        if formset.is_valid():
            videos = formset.save( commit = False )
            for video in videos:
                video.user = request.user
                video.save()

            formset = VideoFormSet( queryset = Video.objects.none() )

            updated_videos = list()
            for video in videos:
                updated_videos.append( Video.objects.get( pk = video.id ) )
            #return HttpResponseRedirect( "/yourphotos" )
            return {
                    "formsets": formset,
                    "completed": True,
                    "videos": updated_videos
            }

            # Do something.
        return {
                "formsets": formset,
                "errors": True
        }
    else:
        formset = VideoFormSet( queryset = Video.objects.none() )
    return {
        "formsets": formset,
    }
