from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns( '',
    ( r'' , include( 'main.urls' ) ),
    ( r'^tinymce/', include( 'tinymce.urls' ) ),
    url(r'^social/', include('socialregistration.urls')),
    ( r'^login/$', 'django.views.generic.simple.direct_to_template', {'template': 'login.html'} ),
    ( r'^locations/', include( 'locations.urls' ) ),
    ( r'^events/', include( 'events.urls' ) ),
    ( r'^people/', include( 'people.urls' ) ),
    ( r'^yourphotos/', include( 'yourphotos.urls' ) ),
    ( r'^videos/', include( 'yourvideos.urls' ) ),
    ( r'^search/', include( 'googlesearch.urls' ) ),
    ( r'^subscribe/', include( 'subscribe.urls' ) ),

    ( r'^magazine/$',  "magazine.views.index" ),

    ( r'^about/$', 'django.views.generic.simple.direct_to_template', {'template': 'static/aboutus.html'} ),
    ( r'^terms_of_use/$', 'django.views.generic.simple.direct_to_template', {'template': 'static/term_of_use.html'} ),

    ( r'^about/partners$', 'django.views.generic.simple.direct_to_template', {'template': 'static/partners.html'} ),

    ( r'^about/products/newsletter$', 'django.views.generic.simple.direct_to_template', {'template': 'static/newsletter.html'} ),
    ( r'^about/products/notebook$', 'django.views.generic.simple.direct_to_template', {'template': 'static/notebook.html'} ),
    ( r'^about/products/events$', 'django.views.generic.simple.direct_to_template', {'template': 'static/events.html'} ),
    ( r'^about/products/magazine$', 'django.views.generic.simple.direct_to_template', {'template': 'static/magazine.html'} ),
    ( r'^about/products/web$', 'django.views.generic.simple.direct_to_template', {'template': 'static/web.html'} ),

    #extra_context



    url( r'^news/add', "news.views.add", {'type': 'news'} ),
    url( r'^news/blog/add', "news.views.add", {'type': 'blog'} ),

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

    ( r'^admin/', include( 'preferences.urls' ) ),
    ( r'^grappelli/', include( 'grappelli.urls' ) ),
    # Uncomment the next line to enable the admin:
    ( r'^admin/', include( admin.site.urls ) ),
    #( r'^photologue/', include( 'photologue.urls' ) ),
 )


if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
