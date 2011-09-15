from decorators import render_to

@render_to( "erumba/index.html" )
def index(request):
    return {}
