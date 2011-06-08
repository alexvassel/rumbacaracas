from django.conf.urls.defaults import *

urlpatterns = patterns( 'yourvideos.views',
    ( r'^$', 'index' ),
    ( r'^add$', 'add' ),
    ( r'^delete/(?P<id>\d+)$', 'delete' ),
    ( r'^(?P<id>\d+)$', 'detail' ),
 )
