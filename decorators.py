from django.template import RequestContext
from django.shortcuts import render_to_response

from django.http import HttpResponse
from django.utils import simplejson
from django.core.mail import mail_admins
from django.utils.translation import ugettext as _
import sys



def render_response( req, *args, **kwargs ):
    kwargs['context_instance'] = RequestContext( req )
    return render_to_response( *args, **kwargs )


def render_to( tmpl ):
    """
    Decorator for Django views that sends returned dict to render_to_response function
    with given template and RequestContext as context instance.

    If view doesn't return dict then decorator simply returns output.
    """
    def renderer( func ):
        def wrapper( request, *args, **kw ):
            output = func( request, *args, **kw )
            if not isinstance( output, dict ):
                return output
            return render_response( request, tmpl, output )
        return wrapper
    return renderer



def json_view( func ):
    def wrap( request, *a, **kw ):
        response = None
        try:
            response = func( request, *a, **kw )
            assert isinstance( response, dict )
            if 'success' not in response:
                response['success'] = True
        except KeyboardInterrupt:
            # Allow keyboard interrupts through for debugging.
            raise
        except Exception, e:
            # Mail the admins with the error
            exc_info = sys.exc_info()
            subject = 'JSON view error: %s' % request.path
            try:
                request_repr = repr( request )
            except:
                request_repr = 'Request repr() unavailable'
            import traceback
            message = 'Traceback:\n%s\n\nRequest:\n%s' % ( 
                '\n'.join( traceback.format_exception( *exc_info ) ),
                request_repr,
                )
            mail_admins( subject, message, fail_silently = True )

            # Come what may, we're returning JSON.
            if hasattr( e, 'message' ):
                msg = e.message
            else:
                msg = _( 'Internal error' ) + ': ' + str( e )
            response = {'success': False,
                        'text': msg}

        json = simplejson.dumps( response )
        return HttpResponse( json, mimetype = 'application/json' )
    return wrap


from hashlib import sha1
from django.core.cache import cache as _djcache
def cache(seconds = 900):
    """
        Cache the result of a function call for the specified number of seconds,
        using Django's caching mechanism.
        Assumes that the function never returns None (as the cache returns None to indicate a miss), and that the function's result only depends on its parameters.
        Note that the ordering of parameters is important. e.g. myFunction(x = 1, y = 2), myFunction(y = 2, x = 1), and myFunction(1,2) will each be cached separately.

        Usage:

        @cache(600)
        def myExpensiveMethod(parm1, parm2, parm3):
            ....
            return expensiveResult
`
    """
    def doCache(f):
        def x(*args, **kwargs):
                key = sha1(str(f.__module__) + str(f.__name__) + str(args) + str(kwargs)).hexdigest()
                result = _djcache.get(key)
                if result is None:
                    result = f(*args, **kwargs)
                    _djcache.set(key, result, seconds)
                return result
        return x
    return doCache
