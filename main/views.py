from django.shortcuts import render_to_response, get_object_or_404, redirect
from zinnia.models import Entry
from events.models import Event
from yourvideos.models import Video
from locations.models import Location
from people.models import PhotoEvent
from yourphotos.models import Photo
from django.utils.translation import ugettext as _
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from decorators import render_to, json_view
from django.forms import ModelForm
from django.forms.models import modelformset_factory
from django.http import HttpResponseRedirect
from datetime import *;
from dateutil.relativedelta import *

from preferences import preferences



from socialregistration.views import setup
from django.views.decorators.csrf import csrf_protect
from django.template.defaultfilters import slugify
from main.forms import UserForm

@csrf_protect
def custom_social_setup( request, template="socialregistration/setup.html" ):
    initial = dict()
    try:
        if request.facebook.uid is not None:
            initial=request.facebook.graph.get_object('me')
            if "username" not in initial:
                initial['username'] = slugify(initial['name'])
    except :
        pass
    return setup(request, initial=initial,form_class=UserForm,template=template)


@render_to( 'main/index.html' )
def index( request ):
    current_date = datetime.today()

    main_image_slider_mode = preferences.MainSliderPreferences.status

    if main_image_slider_mode == "1":
        get_events = 5
        get_news = 0
    elif main_image_slider_mode == "2":
        get_events = 0
        get_news = 5
    else:
        get_events = 3
        get_news = 2

    event_qs = Event.objects.filter( show_in_main_slider = True )
    event_slides = Event.objects.get_occuriences( start_date = current_date, end_date = current_date , qs = event_qs )

    def sortEventList( list ):
        list.sort( key = lambda a:a.position, reverse = False )
        return list

    events_slides = sortEventList( [event for event, date in event_slides] )[:get_events]

    if get_events== 3 and (len(events_slides) < get_events):
        get_news = 5 - len(events_slides)

    blog_slides = Entry.published.filter( show_in_main_slider = True ).order_by( '-creation_date' )[:get_news]

    videos = Video.objects.filter( status = 1 ).order_by( '-datetime_added' )[:5]

    blog = Entry.published.filter(categories__slug = "blog").order_by( '-creation_date' )[:4]
    news = Entry.published.exclude(categories__slug = "blog").order_by( '-creation_date' )[:4]

    locations = Location.objects.filter( status = 1 ).order_by( '?' )[:4]


    art_culture_qs = Event.objects.filter(category=7)
    art_culture_raw = Event.objects.get_occuriences( start_date = current_date, end_date = current_date , qs = art_culture_qs )

    art_culture = sortEventList( [event for event, date in art_culture_raw] )[:4]

    people = PhotoEvent.objects.filter( status = 1 ).order_by( '-date' )[:40]

    photos = Photo.objects.filter( status = 1 ).order_by( '-datetime_added' )[:40]
    
    return {'people': people, 'news': news,'blog': blog,'locations': locations, 'art_culture': art_culture,
            'videos':videos, 'photos': photos,
            'slides': [( blog, 'blog', ) for blog in blog_slides] + [( event, 'event', ) for event in events_slides] }


from django.views.decorators.csrf import requires_csrf_token
from django.http import HttpResponseNotFound
@requires_csrf_token
def page_not_found(request, template_name='404.html'):

    if not request.META.has_key('HTTP_REFERER'):
        return HttpResponseNotFound()

    t = loader.get_template(template_name) # You need to create a 404.html template.

    return HttpResponseNotFound(t.render(RequestContext(request, {'request_path': request.path})))


