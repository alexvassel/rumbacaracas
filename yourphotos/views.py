from django.shortcuts import get_object_or_404
from yourphotos.models import Photo
from django.utils.translation import ugettext as _
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from decorators import render_to
from django.forms import ModelForm
from django.forms.models import modelformset_factory
from django.http import HttpResponseRedirect

@render_to( 'yourphotos/index.html' )
def photos( request, category ):

    try:
        page = int( request.GET.get( 'page', '1' ) )
    except ValueError:
        page = 1

    request.breadcrumbs( _( 'Your Photos' ) , '/yourphotos' )

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

    latest = Photo.objects.filter( status = 1 ).latest( 'datetime_added' )

    return {'latest': latest, 'current_page': photos_page, 'current_paginator': paginator, 'active_tab': category}


@render_to( 'yourphotos/details.html' )
def detail( request , id ):
    photo = get_object_or_404( Photo, pk = id )
    request.breadcrumbs( _( 'Your Photos' ) , '/yourphotos' )
    request.breadcrumbs( photo.description , request.path_info )
    return {'photo': photo}


@render_to( 'yourphotos/add.html' )
def add( request ):
    request.breadcrumbs( _( 'Your Photos' ) , '/yourphotos' )
    request.breadcrumbs( _( 'Add Photos' ) , request.path_info )

    PhotoFormSet = modelformset_factory( Photo, fields = ( 'image', 'description' ), extra = 5, max_num = 5 )
    if request.method == "POST":
        formset = PhotoFormSet( request.POST, request.FILES,
                                queryset = Photo.objects.none() )
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect( "/yourphotos" )
            # Do something.
    else:
        formset = PhotoFormSet( queryset = Photo.objects.none() )
    return {
        "formsets": formset,
    }
