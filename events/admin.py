from events.models import EventCategory, Event, WeekDay
from django.contrib import admin
from sortable.admin import SortableAdmin
from django.utils.translation import ugettext_lazy as _
from django.template.response import TemplateResponse
from django.core.exceptions import PermissionDenied
from django.contrib.admin import helpers
from django.contrib.admin.util import get_deleted_objects, model_ngettext
from django.db import router
from django.utils.encoding import force_unicode


def make_published( modeladmin, request, queryset ):
    queryset.update( status = '1' )
make_published.short_description = _( "Mark selected events as published" )

class EventAdmin( SortableAdmin ):
    prepopulated_fields = {"slug": ( "title", )}
    search_fields = ['title']
    filter_horizontal = ( "repeat", )
    list_display = SortableAdmin.list_display + ( 'title', 'view', 'category', 'get_dates', 'status', 'show_in_events_slider', 'show_in_main_slider', )
    list_editable = SortableAdmin.list_editable + ( 'status', 'show_in_events_slider', 'show_in_main_slider', )
    list_display_links = ( 'title', )
    list_filter = ( 'status', 'show_in_events_slider', 'show_in_main_slider', 'from_date', 'to_date', 'category' )
    date_hierarchy = 'from_date'
    ordering = ('-from_date',)
    actions = [make_published, 'really_delete_selected']
    #ordering = ( 'position', )
    readonly_fields = ( 'add_user', )
    fields = ( 
        'title',
        'slug',
        'category',
        'from_date',
        'to_date',
        'repeat',
        'time',
        'location',
        'place',
        'address',
        'city',
        'area',
        'price',
        'phone',
        'url',
        'email',
        'music',
        'position',
        'image',
        'slider_image',
        'user',
        'description',
        'status',
        'show_in_events_slider', 'show_in_main_slider',
        'add_user',
    )

class EventCategoryAdmin( SortableAdmin ):
    #list_editable = SortableAdmin.list_editable + ( 'status', 'show_in_events_slider', 'show_in_main_slider', )
    list_display = SortableAdmin.list_display + ( 'title', )
    list_display_links = ( 'title', )

admin.site.register( Event, EventAdmin )
admin.site.register( WeekDay )
admin.site.register( EventCategory, EventCategoryAdmin )

