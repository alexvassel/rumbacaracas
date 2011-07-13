from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns( 'subscribe.views',
    ( r'^$', 'subscribe'),
    ( r'^done$', direct_to_template, {'template': 'subscribe/done.html'} ),
 )
