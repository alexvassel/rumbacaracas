from events.models import EventCategory, Event, WeekDay
from django.contrib import admin

class EventAdmin( admin.ModelAdmin ):
    prepopulated_fields = {"slug": ( "title", )}
    filter_horizontal = ( "repeat", )
    list_display = ( 'title', 'view', 'category', )
    list_display_links = ( 'title', )
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
        'sort_order',
        'image',
        'user',
        'description',
    )

admin.site.register( Event, EventAdmin )
admin.site.register( WeekDay )
admin.site.register( EventCategory )

