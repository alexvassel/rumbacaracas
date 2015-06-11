from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings


handler404 = 'main.views.page_not_found'
admin.autodiscover()

urlpatterns = patterns( '',
    ( r'' , include( 'main.urls' ) ),
    ( r'^get_banner/(?P<zone_id>.*)$' ,  'main.views.get_banner'  ),
    ( r'^tinymce/', include( 'tinymce.urls' ) ),
    #Changes in setup proccess
    url(r'^social/setup', 'main.views.custom_social_setup', name='socialregistration_setup'),
    #/Changes in setup proccess

    url(r'^social/', include('socialregistration.urls')),
    ( r'^login/$', 'django.views.generic.simple.direct_to_template', {'template': 'login.html'} ),
    ( r'^locales/', include( 'locations.urls' ) ),
    ( r'^eventos/', include( 'events.urls' ) ),
    ( r'^fotos/', include( 'people.urls' ) ),
    ( r'^tus-fotos/', include( 'yourphotos.urls' ) ),
    ( r'^videos/', include( 'yourvideos.urls' ) ),
    ( r'^facebook/login/', 'django.views.generic.simple.direct_to_template', {'template': 'facebook/login.html'} ),
    ( r'^facebook/setup/', 'facebook_app.views.custom_social_setup', {'template': 'facebook/setup.html'} ),
    ( r'^facebook/', include ( 'facebook_app.urls' ) ),
    
    url(r'^busqueda/resultados/$', 'django.views.generic.simple.direct_to_template', {'template': 'googlesearch/googlesearch_results.html', 'extra_context': {'title' : 'Search Results'}}, name='googlesearch_results'),
    
    ( r'^suscribete/', include( 'subscribe.urls' ) ),

    url( r'^e-rumba/$', "erumba.views.index", name="e_rumba" ),
    url( r'^e-rumba/setup/$', "erumba.views.setup", name="e_rumba_setup" ),

    url( r'^revista/$',  "magazine.views.index", name="magazine_main" ),

    url( r'^nosotros/$', 'django.views.generic.simple.direct_to_template', {'template': 'static/aboutus.html'}, name="about_main" ),
    url( r'^terminos_de_uso/$', 'django.views.generic.simple.direct_to_template', {'template': 'static/term_of_use.html'}, name="terms_of_use" ),

    url( r'^nosotros/alianzas$', 'django.views.generic.simple.direct_to_template', {'template': 'static/partners.html'}, name="about_partners" ),
    url( r'^nosotros/contactos$', 'django.views.generic.simple.direct_to_template', {'template': 'static/contacts.html'}, name="about_contacts" ),
    url( r'^nosotros/productos$', 'django.views.generic.simple.direct_to_template', {'template': 'static/newsletter.html'}, name="about_products" ),
    url( r'^nosotros/productos/boletine_electronico$', 'django.views.generic.simple.direct_to_template', {'template': 'static/newsletter.html'}, name="about_products_news" ),
    #( r'^about/products/notebook$', 'django.views.generic.simple.direct_to_template', {'template': 'static/notebook.html'} ),
    url( r'^nosotros/productos/eventos$', 'django.views.generic.simple.direct_to_template', {'template': 'static/events.html'}, name="about_products_events" ),
    url( r'^nosotros/productos/ediciones_impresas$', 'django.views.generic.simple.direct_to_template', {'template': 'static/magazine.html'}, name="about_products_magazine" ),
    url( r'^nosotros/productos/web$', 'django.views.generic.simple.direct_to_template', {'template': 'static/web.html'} , name="about_products_web"),

    #extra_context

    url( r'^splash$', 'django.views.generic.simple.direct_to_template', {'template': 'splash.html'} , name="splash_page"),


    url( r'^noticias/publica', "news.views.add", {'type': 'news'}, name='news_add' ),
    url( r'^noticias/blog/publica', "news.views.add", {'type': 'blog'}, name='news_add_blog' ),
    
    url(r'^noticias/etiquetas/', include('zinnia.urls.tags')),
    url(r'^noticias/autores/', include('zinnia.urls.authors')),
    url(r'^noticias/categorias/', include('zinnia.urls.categories')),
    url(r'^noticias/', include('zinnia.urls.quick_entry')),
    url(r'^noticias/', include('zinnia.urls.entries')),

    url(r'^trackback/', include('zinnia.urls.trackback')),
    url(r'^noticias/alimenta/', include('zinnia.urls.feeds')),
    url(r'^noticias/discusiones/', include('zinnia.urls.discussions')),



    url( r'^comentarios/', include( 'django.contrib.comments.urls' ) ),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    ( r'^admin/', include( 'preferences.urls' ) ),
    #(r'^tinymce/', include('tinymce.urls')),
    ( r'^grappelli/', include( 'grappelli.urls' ) ),
    # Uncomment the next line to enable the admin:
    ( r'^admin/', include( admin.site.urls ) ),
    #( r'^photologue/', include( 'photologue.urls' ) ),
    
    url( r'^profile/(?P<profile_id>\w+)/$', 'news.views.ath_profile', name = "ath_profile" ),#added for authors profile view
 )


if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            'show_indexes': True
        }),
   )
