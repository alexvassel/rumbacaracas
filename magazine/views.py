from decorators import render_to
from preferences import preferences
from django.utils.safestring import mark_safe

@render_to( 'magazine/magazine.html' )
def index( request ):

    last_magazine_anotate = preferences.LastMagazinePreferences.anotation

    return {'last_magazine_anotate': mark_safe(last_magazine_anotate)}


