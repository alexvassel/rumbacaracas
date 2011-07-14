from people.models import PhotoEvent, Photo
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


def make_published( modeladmin, request, queryset ):
    queryset.update( status = '1' )
make_published.short_description = _( "Mark selected photos as published" )


class PhotoInline( admin.TabularInline ):
    model = Photo
    readonly_fields = ( 'thumb_tag', 'make_main_tag' )


class EventAdmin( admin.ModelAdmin ):
    prepopulated_fields = {"slug": ( "title", )}
    list_display = ( 'title', 'category', 'import_photo', 'status' )

    inlines = [
        PhotoInline,
    ]
    actions = [make_published]
    class Media:
        js = ("/media/js/people_admin_hacks.js",)

admin.site.register( PhotoEvent, EventAdmin )

