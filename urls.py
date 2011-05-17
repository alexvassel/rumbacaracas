from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns( '',
    ( r'' , include( 'yourphotos.urls' ) ),
    ( r'^social/', include( 'socialregistration.urls' ) ),
    ( r'^login/$', 'django.views.generic.simple.direct_to_template', {'template': 'login.html'} ),
    ( r'^locations/', include( 'locations.urls' ) ),
    ( r'^events/', include( 'events.urls' ) ),
    ( r'^peoples/', include( 'peoples.urls' ) ),
    ( r'^yourphotos/', include( 'yourphotos.urls' ) ),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     ( r'^admin/', include( admin.site.urls ) ),
     #( r'^photologue/', include( 'photologue.urls' ) ),
     ( r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_DOC_ROOT} ),
 )



