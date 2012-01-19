from events.models import EventCategory, Event, WeekDay
from django.contrib import admin
from sortable.admin import SortableAdmin
from django.utils.translation import ugettext_lazy as _
from django.template.response import TemplateResponse


def make_published( modeladmin, request, queryset ):
    queryset.update( status = '1' )
make_published.short_description = _( "Mark selected events as published" )

class EventAdmin( SortableAdmin ):
    actions=[]
    def get_actions(self, request):
        actions = super(EventAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    
    
    def really_delete_selected(self, request, queryset):
        for obj in queryset:
            print str(obj.slug)
            from django.db import connections, transaction
            cursor = connections['venezuela'].cursor()
            query = "DELETE FROM events_event WHERE slug='"+str(obj.slug)+"'"
            cursor.execute(query)
            transaction.commit_unless_managed(using='venezuela')
            
            print query
            obj.delete()

        if queryset.count() == 1:
            message_bit = "1 photoblog entry was"
        else:
            message_bit = "%s photoblog entries were" % queryset.count()
        self.message_user(request, "%s successfully deleted." % message_bit)
        
        
        context = {
            "title": "Events",
            'queryset': queryset
        }
        return TemplateResponse(request, EventAdmin.delete_selected_confirmation_template or [
            "admin/%s/%s/delete_selected_confirmation.html" % ('Events', 'wWwWw'),
            "admin/%s/delete_selected_confirmation.html" % 'Events',
            "admin/delete_selected_confirmation.html"
            ], context, current_app='Events')
        
    really_delete_selected.short_description = "Delete selected entries"
    
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

