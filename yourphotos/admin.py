from yourphotos.models import  Photo
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

def make_published( modeladmin, request, queryset ):
    queryset.update( status = '1' )
make_published.short_description = _( "Mark selected photos as published" )


class PhotoAdmin( admin.ModelAdmin ):
    search_fields = ['description']
    list_display = ( 'thumb', 'user', 'description', 'category', 'datetime_added', 'status' )
    list_editable = ( 'description', 'category', 'status' )
    list_filter = ( 'status', )
    actions = [make_published]

admin.site.register( Photo, PhotoAdmin )
