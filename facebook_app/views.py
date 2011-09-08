from decorators import render_to
import itertools
from django.http import HttpResponseRedirect
from main.modelFields import SlugifyUniquely
from django.core.urlresolvers import reverse
from events.models import Event, EventCategory
from yourphotos.models import Photo
import urllib2
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.contrib.auth.decorators import login_required

import dateutil.parser

@render_to( 'facebook/events_list.html' )
def events_list(request):

    graph = request.facebook.graph
    user  = graph.get_object("me")

    if request.method == 'POST':
        events_ids = request.POST.getlist("object_events")

        for event_id in events_ids:
            event = graph.get_object(event_id)
            image_url = "https://graph.facebook.com/" + event["id"] + "/picture?type=large"

            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(urllib2.urlopen(image_url).read())
            img_temp.flush()

            user_event = Event(
                title = event["name"],
                from_date = dateutil.parser.parse(event["start_time"]),
                to_date = dateutil.parser.parse(event["end_time"]),
                address = event["location"],
                description = event["description"],
                user = request.user,
                category = EventCategory.objects.get(id=1),
                status = 2,
            )

            user_event.image.save(event["id"] + ".jpg", File(img_temp));
            user_event.slug = SlugifyUniquely( event["name"], user_event.__class__)
            user_event.save()

        return HttpResponseRedirect( reverse('facebook_events_list') )

    events = graph.get_connections(user["id"], "events")

    for event in events["data"]:
        event["start_time"] = dateutil.parser.parse(event["start_time"])
        event["end_time"] = dateutil.parser.parse(event["end_time"])
        event["picture_url"] = "https://graph.facebook.com/" + event["id"] + "/picture?type=normal"

    return dict(
        user = user,
        events = events,
    )

@render_to( 'facebook/albums_list.html' )
def albums_list(request):

    graph = request.facebook.graph
    user = graph.get_object("me")
    albums = graph.get_connections(user["id"], "albums")

    for album in albums["data"]:
        album["picture_url"] = "https://graph.facebook.com/" + album["id"] + "/picture?type=small"

    return dict(
        user = user,
        albums = albums,
    )

@render_to( 'facebook/photos_list.html' )
def photos_list(request, id):

    graph = request.facebook.graph
    user = graph.get_object("me")

    if request.method == 'POST':
        photos_ids = request.POST.getlist("object_photos")

        for photo_id in photos_ids:

            photo = graph.get_object(photo_id)

            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(urllib2.urlopen(photo["source"]).read())
            img_temp.flush()

            user_photo = Photo(
                user = request.user,
            )

            #if photo.

            user_photo.image.save(photo["id"] + "." + (photo["source"].split(".")[-1]), File(img_temp));
            user_photo.save()

        return HttpResponseRedirect( reverse('facebook_photos_list', args=[id]) )

    album = graph.get_object(id)
    photos = graph.get_connections(album["id"], "photos")

    return dict(
        user = user,
        album = album,
        photos = photos,
    )
