from yourvideos.models import  Video
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

def make_published( modeladmin, request, queryset ):
    queryset.update( status = '1' )
make_published.short_description = _( "Mark selected videos as published" )

class VideoAdmin( admin.ModelAdmin ):
    search_fields = ['description']
    list_display = ( 'thumb', 'description', 'datetime_added', 'status' )
    list_editable = ( 'description', 'status' )
    list_filter = ( 'status', )
    readonly_fields = ( 'video', )
    #fieldsets = [
    #    ( _( 'Main data' ), {'fields': ( 
    #        'user', 'youtube_id', 'description', 'status',
    #    )} ),
    #    ( _( 'Preview' ), {'fields': ( 'video', )} ),
    #]
    actions = [make_published]

admin.site.register( Video, VideoAdmin )
