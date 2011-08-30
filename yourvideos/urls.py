from django.conf.urls.defaults import *

urlpatterns = patterns( 'yourvideos.views',
    url( r'^$', 'index', name="video_main" ),
    url( r'^publica$', 'add', name="video_add" ),
    url( r'^borrar/(?P<id>\d+)$', 'delete', name="video_delete" ),
    url( r'^(?P<id>\d+)$', 'detail' , name = "video_details" ),
 )
