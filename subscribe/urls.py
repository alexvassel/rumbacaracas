from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns( 'subscribe.views',
    url( r'^$', 'subscribe', name="subscribe_main"),
    url( r'^hecho$', direct_to_template, {'template': 'subscribe/done.html'}, name="subscribe_done" ),
 )
