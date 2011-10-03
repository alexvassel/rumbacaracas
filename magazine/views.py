from decorators import render_to
from preferences import preferences
from django.utils.safestring import mark_safe
from django.conf import settings
import hashlib
import urllib
from datetime import date
import re

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

def _get_issuu_folders_list():

    args = {}
    args['action'] = "issuu.folders.list"
    args['apiKey'] = settings.ISSUU_API_KEY
    args['startIndex'] = "0"
    args['pageSize'] = "30"
    args['format'] = "json"
    args['folderSortBy'] = "created"
    args['resultOrder'] = "desc"

    m = hashlib.md5()
    sec_string = settings.ISSUU_API_SECRET + ''.join([key + args[key] for key in sorted(args.iterkeys())]);
    m.update(sec_string)

    signature = m.hexdigest()
    args['signature'] = signature

    request_url = "http://api.issuu.com/1_0?" + urllib.urlencode(args)
    file = urllib.urlopen(request_url)
    response = _parse_json(file.read())

    return response['rsp']['_content']['result']['_content']


def _get_issuu_last_document():

    args = {}
    args['action'] = "issuu.documents.list"
    args['apiKey'] = settings.ISSUU_API_KEY
    args['startIndex'] = "0"
    args['pageSize'] = "1"
    args['format'] = "json"
    args['folderSortBy'] = "created"
    args['resultOrder'] = "desc"
    args['documentStates'] = "A"

    m = hashlib.md5()
    sec_string = settings.ISSUU_API_SECRET + ''.join([key + args[key] for key in sorted(args.iterkeys())]);
    m.update(sec_string)

    signature = m.hexdigest()
    args['signature'] = signature

    request_url = "http://api.issuu.com/1_0?" + urllib.urlencode(args)
    file = urllib.urlopen(request_url)
    response = _parse_json(file.read())

    return response['rsp']['_content']['result']['_content'][0]['document']

@render_to( 'magazine/magazine.html' )
def index( request ):

    item_year = date.today().year

    folders_list = _get_issuu_folders_list()
    albums    = filter(lambda a: a['folder']['itemCount'] > 0 and re.match('^\d{4}$', a['folder']['name']), folders_list)

    default_album = None
    for album in albums:
        if item_year == int(album['folder']['name']):
            default_album = album

    default_notebook = None
    notebooks = filter(lambda a: a['folder']['itemCount'] > 0 and re.match('^Notebook \d{4}$', a['folder']['name']), folders_list)
    for notebook in notebooks:
        name = notebook['folder']['name'].replace('Notebook ')
        if item_year == int(name):
            default_notebook = notebook

    last_magazine_anotate = preferences.LastMagazinePreferences.anotation
    last_magazine_issuu_code = preferences.LastMagazinePreferences.issuu_code

    return {
        'last_magazine_anotate': mark_safe(last_magazine_anotate),
        'albums': albums,
        'notebooks': notebooks,
        'last_magazine_issuu_code' : last_magazine_issuu_code,
        'default_notebook': default_notebook,
        'default_album': default_album
    }

