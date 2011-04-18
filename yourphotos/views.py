from django.shortcuts import get_object_or_404
from yourphotos.models import Photo, PhotoCategory
from django.utils.translation import ugettext as _
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from decorators import render_to


@render_to( 'locations/index.html' )
def photos( request ):
    request.breadcrumbs( _( 'Your Photos' ) , '/yourphotos' )
    #request.breadcrumbs( _( 'By Category' ) , request.path_info )

    main = Photo.objects.order_by( '?' )[:1].first()

    return {'main': main, }

