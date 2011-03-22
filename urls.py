from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns( '',
    # Example:
    # (r'^rumbabogota/', include('rumbabogota.foo.urls')),
    ( r'^locations/', include( 'locations.urls' ) ),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     ( r'^admin/', include( admin.site.urls ) ),
     #( r'^photologue/', include( 'photologue.urls' ) ),
     ( r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_DOC_ROOT} ),
 )



