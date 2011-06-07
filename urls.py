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
    ( r'^people/', include( 'people.urls' ) ),
    ( r'^yourphotos/', include( 'yourphotos.urls' ) ),

    url( r'^news/add', "news.views.add" ),

    url( r'^news/', include( 'zinnia.urls' ) ),

    #url(r'^trackback/', include('zinnia.urls.trackback')),
    #url(r'^news/tags/', include('zinnia.urls.tags')),
    #url(r'^news/feeds/', include('zinnia.urls.feeds')),
    #url(r'^news/authors/', include('zinnia.urls.authors')),
    #url(r'^news/categories/', include('zinnia.urls.categories')),
    #url(r'^news/discussions/', include('zinnia.urls.discussions')),
    #url(r'^news/', include('zinnia.urls.quick_entry')),
    #url(r'^news/', include('zinnia.urls.entries')),

    url( r'^comments/', include( 'django.contrib.comments.urls' ) ),



    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    ( r'^grappelli/', include( 'grappelli.urls' ) ),
    # Uncomment the next line to enable the admin:
     ( r'^admin/', include( admin.site.urls ) ),
     #( r'^photologue/', include( 'photologue.urls' ) ),
     ( r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_DOC_ROOT} ),
 )



