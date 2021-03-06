from people.models import PhotoEvent, Photo, EventRequest
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


def make_published( modeladmin, request, queryset ):
    queryset.update( status = '1' )
make_published.short_description = _( "Mark selected photos as published" )


class PhotoInline( admin.TabularInline ):
    model = Photo
    readonly_fields = ( 'thumb_tag', 'make_main_tag' )


class EventAdmin( admin.ModelAdmin ):
    search_fields = ['title']
    prepopulated_fields = {"slug": ( "title", )}
    list_display = ( 'title', 'category','status', )
    change_form_template = "people/admin_change_form.html"
    inlines = [
        PhotoInline,
    ]
    actions = [make_published]

    class Media:
        js = ("/media/js/people_admin_hacks.js",)

class ReuestAdmin( admin.ModelAdmin ):
    list_display = ( 'name', 'category', 'date', 'time' , 'city', 'address', 'datetime_added', )
    list_display_links = ( 'name', )

admin.site.register( PhotoEvent, EventAdmin )
admin.site.register( EventRequest, ReuestAdmin)

