from django.shortcuts import render_to_response, get_object_or_404, redirect
from main.models import Slide
from zinnia.models import Entry
from events.models import Event
from django.utils.translation import ugettext as _
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from decorators import render_to, json_view
from django.forms import ModelForm
from django.forms.models import modelformset_factory
from django.http import HttpResponseRedirect
from datetime import *;
from dateutil.relativedelta import *

from preferences import preferences

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

    def sortList( list ):
        list.sort( key = lambda a:a.position, reverse = False )
        return list

    events_slides = sortList( [event for event, date in event_slides] )[:get_events]
    blog_slides = Entry.published.filter( show_in_main_slider = True ).order_by( '-creation_date' )[:get_news]

    return {'slides': [( blog, 'blog', ) for blog in blog_slides] + [( event, 'event', ) for event in events_slides] }

