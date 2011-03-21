from events.models import EventCategory, Event, DressType, WeekDay
from django.contrib import admin

class EventAdmin( admin.ModelAdmin ):
    filter_horizontal = ( "repeat", )


admin.site.register( Event, EventAdmin )


admin.site.register( WeekDay )
admin.site.register( EventCategory )
admin.site.register( DressType )

