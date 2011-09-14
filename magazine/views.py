from decorators import render_to
from preferences import preferences
from django.utils.safestring import mark_safe
import hashlib
import settings
import urllib

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

    folders_list = _get_issuu_folders_list()
    albums    = filter(lambda a: a['folder']['itemCount'] > 0 and "notebook" not in a['folder']['name'], folders_list)
    notebooks = filter(lambda a: a['folder']['itemCount'] > 0 and "notebook"     in a['folder']['name'], folders_list)
    last_magazine_anotate = preferences.LastMagazinePreferences.anotation
    #last_magazine_anotate = _get_issuu_last_document()

    return {'last_magazine_anotate': mark_safe(last_magazine_anotate), 'albums': albums, 'notebooks': notebooks}


