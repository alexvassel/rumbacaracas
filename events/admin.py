from events.models import EventCategory, Event, WeekDay
from django.contrib import admin

class EventAdmin( admin.ModelAdmin ):
    prepopulated_fields = {"slug": ( "title", )}
    filter_horizontal = ( "repeat", )
    list_display = ( 'title', 'view', 'category', )
    list_display_links = ( 'title', )


admin.site.register( Event, EventAdmin )
admin.site.register( WeekDay )
admin.site.register( EventCategory )

