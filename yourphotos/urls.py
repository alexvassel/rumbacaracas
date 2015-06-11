from django.conf.urls.defaults import *

urlpatterns = patterns( 'yourphotos.views',
    url( r'^$', 'photos', {'category': 'latest'}, name = "yourphoto_main"  ),
    url( r'^publica$', 'add', name = "yourphoto_add"  ),
    url( r'^borrar/(?P<id>\d+)$', 'delete', name = "yourphoto_delete"  ),

    url( r'^ultimas$', 'photos', {'category': 'latest'}, name = "yourphoto_category_latest" ),
    url( r'^sexy$', 'photos', {'category': 'sexy'}, name = "yourphoto_category_sexy" ),
    url( r'^rumbas$', 'photos', {'category': 'rumbas'}, name = "yourphoto_category_rumbas" ),
    url( r'^amigos$', 'photos', {'category': 'amigos'}, name = "yourphoto_category_amigos" ),
    url( r'^humor$', 'photos', {'category': 'humor'}, name = "yourphoto_category_humor" ),
    

    url( r'^main_slide/(?P<photo_id>\d+)$', 'main_slide', name = "yourphoto_main_slide" ),
    url( r'^(?P<id>\d+)$', 'detail' , name = "yourphoto_details" ),
 )
