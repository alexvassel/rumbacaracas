import base64, hashlib, hmac, json, urllib, time
from socialregistration.models import FacebookProfile
from socialregistration.views import _get_next
import facebook
import md5
from django.conf import settings
from decorators import render_to
import itertools
from django.http import HttpResponseRedirect, HttpResponse
from main.modelFields import SlugifyUniquely
from django.core.urlresolvers import reverse
from events.models import Event, EventCategory
from yourphotos.models import Photo
import urllib2
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout as auth_logout

from socialregistration.views import setup
from django.views.decorators.csrf import csrf_protect
from django.template.defaultfilters import slugify
from main.forms import UserForm

import dateutil.parser

# Find a JSON parser
try:
    import json
    _parse_json = lambda s: json.loads(s)
except ImportError:
    try:
        import simplejson
        _parse_json = lambda s: simplejson.loads(s)
    except ImportError:
        # For Google AppEngine
        from django.utils import simplejson
        _parse_json = lambda s: simplejson.loads(s)

def _base64_url_decode(data):
    data = data.encode(u'ascii')
    data += '=' * (4 - (len(data) % 4))
    return base64.urlsafe_b64decode(data)

def _add_flash_message(request, message):
    request.session['_flash_message'] = message

def _get_flash_message(request):
    if "_flash_message" in request.session:
        message = request.session['_flash_message']
        del request.session['_flash_message']
        return message

    return None

def _get_next(request):
    """
    Returns a url to redirect to after the login
    """
    if 'next' in request.session:
        next = request.session['next']
        del request.session['next']
        return next
    elif 'next' in request.GET:
        return request.GET.get('next')
    elif 'next' in request.POST:
        return request.POST.get('next')
    else:
        return getattr(settings, 'LOGIN_REDIRECT_URL', '/')

def _init_facebook_app(request):

    # Old method to init app
    if "fb_sig" in request.POST:
        if "access_token" in request.session:
            return False

        fbsig = {}
        for param in request.POST:
            if param.startswith("fb_sig_"):
                fbsig[param[7:]] = request.POST[param]

        secret_string = ""
        for key in sorted(fbsig.iterkeys()):
           secret_string += key + "=" + fbsig[key]

        secret_string += settings.FACEBOOK_SECRET_KEY

        m = md5.new()
        m.update(secret_string)

        if m.hexdigest() == request.POST["fb_sig"]:
            args = {}
            args["display"] = "page"
            args["client_id"] = settings.FACEBOOK_APP_ID
            args["redirect_uri"] = "http://" + request.META["HTTP_HOST"] + "/facebook/"
            args["scope"] = settings.FACEBOOK_REQUEST_PERMISSIONS
            redirect_url = "<script type='text/javascript'>top.location.href='https://www.facebook.com/dialog/oauth?" + urllib.urlencode(args) + "'</script>"
            return HttpResponse(redirect_url)

        return False
    # New method to init app
    elif "signed_request" in request.POST:

        if "access_token" in request.session:
            return False

        sig, payload = request.POST["signed_request"].split(u'.', 1)
        sig = _base64_url_decode(sig)
        data = json.loads(_base64_url_decode(payload))

        expected_sig = hmac.new(
            settings.FACEBOOK_SECRET_KEY, msg=payload, digestmod=hashlib.sha256).digest()

        # allow the signed_request to function for upto 1 day
        if sig == expected_sig and data[u'issued_at'] > (time.time() - 86400):
            args = {}
            args["display"] = "page"
            args["client_id"] = settings.FACEBOOK_APP_ID
            args["redirect_uri"] = "http://" + request.META["HTTP_HOST"] + "/facebook/"
            args["scope"] = settings.FACEBOOK_REQUEST_PERMISSIONS
            redirect_url = "<script type='text/javascript'>top.location.href='https://www.facebook.com/dialog/oauth?" + urllib.urlencode(args) + "'</script>"
            return HttpResponse(redirect_url)

        return False

    if "code" in request.GET:
        args = {}
        args["client_id"] = settings.FACEBOOK_APP_ID
        args["redirect_uri"] = "http://" + request.META["HTTP_HOST"] + "/facebook/"
        args["client_secret"] = settings.FACEBOOK_SECRET_KEY
        args["code"] = request.GET["code"]
        request_url = "https://graph.facebook.com/oauth/access_token?" + urllib.urlencode(args)

        file = urllib.urlopen(request_url)

        response = file.read().split("&")
        for value in response:
            parts = value.split("=")
            request.session[parts[0]] = parts[1]

        return HttpResponseRedirect("http://apps.facebook.com/"+ settings.FACEBOOK_APP_ID +"/")

    return False

def _get_facebook_app(request):
    if "access_token" in request.session:
        graph = facebook.GraphAPI(request.session["access_token"])
        user  = graph.get_object("me")

        sys_user = authenticate(uid=user["id"])
        if sys_user is None:
            request.session['socialregistration_user'] = User()
            request.session['socialregistration_profile'] = FacebookProfile(uid=user["id"])
            request.session['socialregistration_client'] = request.facebook
            request.session['next'] = "http://apps.facebook.com/"+ settings.FACEBOOK_APP_ID +"/"
            return graph, user, None

        login(request, sys_user)

        return graph, user, sys_user

    return None, None, None

@csrf_protect
def custom_social_setup( request, template="socialregistration/setup.html" ):
    func_return = _init_facebook_app(request)
    if(func_return != False):
        return func_return

    initial = dict()
    try:
        graph, initial, sys_user = _get_facebook_app(request)
        if request.facebook.uid is not None:
            if "username" not in initial:
                initial['username'] = slugify(initial['name'])
    except :
        pass
    return setup(request, initial=initial,form_class=UserForm,template=template)

@csrf_exempt
@render_to( 'facebook/events_list.html' )
def events_list(request):

    func_return = _init_facebook_app(request)
    if(func_return != False):
        return func_return

    try:
        graph, user, sys_user = _get_facebook_app(request)
        if sys_user is None:
            return HttpResponseRedirect("/facebook/setup/")
    except facebook.GraphAPIError:
        del request.session["access_token"]
        return HttpResponseRedirect("http://apps.facebook.com/"+ settings.FACEBOOK_APP_ID +"/")

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
                user = sys_user.username,
                add_user = sys_user,
                category = EventCategory.objects.get(id=1),
                status = 2,
            )

            if "description" in event:
                user_event.description = event["description"]

            user_event.image.save(event["id"] + ".jpg", File(img_temp));
            user_event.slug = SlugifyUniquely( event["name"], user_event.__class__)
            user_event.save()

        if len(events_ids) > 0:
            _add_flash_message(request, "Your events has been added")
        return HttpResponseRedirect( reverse('facebook_events_list') )

    events = graph.get_connections(user["id"], "events")

    for event in events["data"]:
        event["start_time"] = dateutil.parser.parse(event["start_time"])
        event["end_time"] = dateutil.parser.parse(event["end_time"])
        event["picture_url"] = "https://graph.facebook.com/" + event["id"] + "/picture?type=normal"

    return dict(
        user = user,
        events = events,
        message = _get_flash_message(request),
    )

@csrf_exempt
#@login_required( login_url = '/facebook/login/' )
@render_to( 'facebook/albums_list.html' )
def albums_list(request):

    func_return = _init_facebook_app(request)
    if(func_return != False):
        return func_return

    try:
        graph, user, sys_user = _get_facebook_app(request)
        if sys_user is None:
            return HttpResponseRedirect("/facebook/setup/")
    except facebook.GraphAPIError:
        del request.session["access_token"]
        return HttpResponseRedirect("http://apps.facebook.com/"+ settings.FACEBOOK_APP_ID +"/")

    albums = graph.get_connections(user["id"], "albums")

    for album in albums["data"]:
        if "cover_photo" in album:
            cover = graph.get_object(album["cover_photo"])
            album["picture_url"] = cover["images"][1]["source"]
        else:
            album["picture_url"] = "https://graph.facebook.com/" + album["id"] + "/picture?type=small"

    return dict(
        user = user,
        albums = albums,
    )

@csrf_exempt
#@login_required( login_url = '/facebook/login/' )
@render_to( 'facebook/photos_list.html' )
def photos_list(request, id):

    func_return = _init_facebook_app(request)
    if(func_return != False):
        return func_return

    try:
        graph, user, sys_user = _get_facebook_app(request)
        if sys_user is None:
            return HttpResponseRedirect("/facebook/setup/")
    except facebook.GraphAPIError:
        del request.session["access_token"]
        return HttpResponseRedirect("http://apps.facebook.com/"+ settings.FACEBOOK_APP_ID +"/")

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

            user_photo.image.save(photo["id"] + "." + (photo["source"].split(".")[-1]), File(img_temp));
            user_photo.save()

        if len(photos_ids) > 0:
            _add_flash_message(request, "Your photos has been added")
        return HttpResponseRedirect( reverse('facebook_photos_list', args=[id]) )

    album = graph.get_object(id)
    photos = graph.get_connections(album["id"], "photos")

    return dict(
        user = user,
        album = album,
        photos = photos,
        message = _get_flash_message(request),
    )
