from django import template
register = template.Library()


@register.inclusion_tag( 'main/facebook_comments.html' )
def display_( url ):
    full_url = settings.FULL_BASE_URL + url
    return dict( url = full_url )
