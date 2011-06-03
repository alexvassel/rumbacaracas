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
    list_display = SortableAdmin.list_display + ( 'title', 'view', 'category', 'status', 'featured', )
    list_editable = SortableAdmin.list_editable + ( 'status', 'featured' )
    list_display_links = ( 'title', )
    list_filter = ( 'status', 'featured', )
    actions = [make_published]
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
        'featured',
        'add_user',
    )

admin.site.register( Event, EventAdmin )
admin.site.register( WeekDay )
admin.site.register( EventCategory )

