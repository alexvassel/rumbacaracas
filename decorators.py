from django.template import RequestContext
from django.shortcuts import render_to_response

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
