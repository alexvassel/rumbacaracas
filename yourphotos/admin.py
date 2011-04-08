from yourphotos.models import PhotoCategory, Photo
from django.contrib import admin

def make_published( modeladmin, request, queryset ):
    queryset.update( status = '1' )
make_published.short_description = "Mark selected photos as published"


class PhotoAdmin( admin.ModelAdmin ):
    list_display = ( 'thumb', 'user', 'description', 'category', 'status' )
    list_editable = ( 'description', 'category', 'status' )
    list_filter = ( 'status', )
    actions = [make_published]

admin.site.register( Photo, PhotoAdmin )
admin.site.register( PhotoCategory )
