from django.conf.urls.defaults import *

urlpatterns = patterns( 'yourphotos.views',
    ( r'^$', 'photos' ),
    ( r'^photos$', 'photos' ),
    ( r'^add$', 'add' ),
    ( r'^(?P<slug>[-\w]+)/$', 'detail' ),
 )
