from events.models import EventCategory, Event, WeekDay
from django.contrib import admin
from sortable.admin import SortableAdmin
from django.utils.translation import ugettext_lazy as _



def make_published( modeladmin, request, queryset ):
    queryset.update( status = '1' )
make_published.short_description = _( "Mark selected events as published" )

class EventAdmin( SortableAdmin ):
    prepopulated_fields = {"slug": ( "title", )}
    filter_horizontal = ( "repeat", )
    list_display = SortableAdmin.list_display + ( 'title', 'view', 'category', 'get_dates', 'status', 'show_in_events_slider', 'show_in_main_slider', )
    list_editable = SortableAdmin.list_editable + ( 'status', 'show_in_events_slider', 'show_in_main_slider', )
    list_display_links = ( 'title', )
    list_filter = ( 'status', 'show_in_events_slider', 'show_in_main_slider', )
    actions = [make_published]
    ordering = ( 'position', )
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
        'user',
        'description',
        'status',
        'show_in_events_slider', 'show_in_main_slider',
        'add_user',
    )

admin.site.register( Event, EventAdmin )
admin.site.register( WeekDay )
admin.site.register( EventCategory )

