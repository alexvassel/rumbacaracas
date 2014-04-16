from django.shortcuts import render_to_response, get_object_or_404, redirect
from zinnia.models import Entry
from events.models import Event, EVENT_ART_CULTURE_CATEGORY
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
from main.models import MostViewed
from events.models import EventCategory
from django.contrib.contenttypes.models import ContentType
from preferences import preferences

import random
import calendar


from socialregistration.views import setup
from django.views.decorators.csrf import csrf_protect
from django.template.defaultfilters import slugify
from main.forms import UserForm
from socialregistration.models import TwitterProfile
from django.conf import settings

@csrf_protect
def custom_social_setup( request, template="socialregistration/setup.html" ):
    initial = dict()
    try:
        if request.facebook.uid is not None:
            initial=request.facebook.graph.get_object('me')
            if "username" not in initial:
                initial['username'] = slugify(initial['name'])
        if request.user is not None:
            import tweepy
            auth = tweepy.OAuthHandler(settings.TWITTER_CONSUMER_KEY, settings.TWITTER_CONSUMER_SECRET_KEY)
            api = tweepy.API(auth)
            twitter_user = TwitterProfile.objects.get( user = request.user )
            twitter_data = api.get_user(user_id=twitter_user.twitter_id)
            initial['username'] = twitter_data.screen_name
    except :
        pass
    return setup(request, initial=initial,form_class=UserForm,template=template)


def upcoming_events_list(count = 2):
    today = datetime.today()
    dtstart = datetime( today.year, today.month, today.day )

    zdat_day = datetime.today() + timedelta(6 - dtstart.weekday())
    dtend = datetime( zdat_day.year, zdat_day.month, zdat_day.day )

    #TODO wrong check if upcoming
    event_list = Event.objects.filter(status=1,to_date__gte = dtstart,to_date__lte = dtend).order_by('to_date')[:count]
    return event_list

def most_viewed_events_list(count=2):
    today = datetime.today()
    dtstart = datetime( today.year, today.month, today.day )
    range_month = calendar.monthrange(today.year, today.month)[1]
    dtend = datetime( today.year, today.month, range_month )
    
    try:
        ct_event = ContentType.objects.get(app_label='events', model='event')
        long_events_catogry_id=EventCategory.objects.filter(title='Promociones').values_list('id', flat=True)
        event_list = list(Event.objects.filter(to_date__gte = dtstart, to_date__lte = dtend,).exclude(category=long_events_catogry_id[0]).values_list('id', flat=True))
        event_list=event_list
        if event_list:
            most_viewed_events = list(MostViewed.objects.filter(content_type=ct_event, content_type_object_id__in=event_list).order_by('-no_of_views').values_list('content_type_object_id', flat=True)[:count])
            
            events = list(Event.objects.filter(id__in = most_viewed_events))
            events.sort( key = lambda a:a.to_date, reverse = True )
        else:
            return []
    except IndexError:
        pass
    return events


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
#     news = Entry.published.exclude(categories__slug = "blog").order_by( '-creation_date' )[:8]
    news = Entry.published.order_by( '-creation_date' )[:8]

    locations = Location.objects.filter( status = 1 ).order_by( '?' )[:4]


    art_culture_qs = Event.objects.filter(category=EVENT_ART_CULTURE_CATEGORY)
    art_culture_raw = Event.objects.get_occuriences( start_date = current_date, end_date = current_date , qs = art_culture_qs )

    art_culture = sortEventList( [event for event, date in art_culture_raw] )[:4]

    people = PhotoEvent.objects.filter( status = 1 ).order_by( '-date' )[:40]

    photos = Photo.objects.filter( status = 1 ).order_by( '-datetime_added' )[:40]

    final_slides = [( blog_tmp, 'blog', ) for blog_tmp in blog_slides] + [( event_tmp, 'event', ) for event_tmp in events_slides]
    random.shuffle(final_slides)
    
    events = upcoming_events_list(2)
    
    ct_news = ContentType.objects.get(app_label='zinnia', model='entry')
#    ct_event = ContentType.objects.get(app_label='events', model='event')
    last_thirty_days_date=datetime.today()-timedelta(days=30)
    entries=Entry.objects.filter(creation_date__gte=last_thirty_days_date)
    most_viewed_news = list(MostViewed.objects.filter(content_type=ct_news,content_type_object_id__in=entries).order_by('-no_of_views').values_list('content_type_object_id', flat=True)[:6])
#    most_viewed_events = list(MostViewed.objects.filter(content_type=ct_event).order_by('-no_of_views').values_list('content_type_object_id', flat=True)[:10])
    m_v_n = []
    for entry in entries:
        if entry.id in most_viewed_news:
            m_v_n.append(entry)
#     m_v_n = list(Entry.objects.filter(id__in=most_viewed_news)[:6:1])
    m_v_n.sort( key = lambda a:a.creation_date, reverse = True )
    m_v_e = most_viewed_events_list(2)
    
    return {'people': people, 'news': news,'blog': blog,'locations': locations, 'art_culture': art_culture,
            'videos':videos, 'photos': photos,
            'slides': final_slides, 'upcomming_events':events, 'most_viewed_news':m_v_n,
            'most_viewed_events':m_v_e}


from django.views.decorators.csrf import requires_csrf_token
from django.http import HttpResponseNotFound
from django.template import Context, RequestContext, loader

@requires_csrf_token
def page_not_found(request, template_name='404.html'):

    if not request.META.has_key('HTTP_REFERER'):
        return HttpResponseNotFound(_('Page not found'))

    t = loader.get_template(template_name) # You need to create a 404.html template.

    return HttpResponseNotFound(t.render(RequestContext(request, {'request_path': request.path})))



@render_to( 'main/openx_banner.html' )
def get_banner( request , zone_id ):
    #if not request.is_ajax():
     #   return HttpResponseRedirect( '/' )
    rand = int(100000 * random.random())
    return dict( zone_id = zone_id, rand =rand  )
