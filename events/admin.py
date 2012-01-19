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
    actions=['really_delete_selected']

    def get_actions(self, request):
        actions = super(EventAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions
    
    def really_delete_selected(modeladmin, request, queryset):
        post = ''
        """
        Default action which deletes the selected objects.
        This action first displays a confirmation page whichs shows all the
        deleteable objects, or, if the user has no permission one of the related
        childs (foreignkeys), a "permission denied" message.
        Next, it delets all selected objects and redirects back to the change list.
        """
        opts = modeladmin.model._meta
        app_label = opts.app_label
        # Check that the user has delete permission for the actual model
        if not modeladmin.has_delete_permission(request):
            raise PermissionDenied
        using = router.db_for_write(modeladmin.model)
        # Populate deletable_objects, a data structure of all related objects that
        # will also be deleted.
        deletable_objects, perms_needed, protected = get_deleted_objects(
            queryset, opts, request.user, modeladmin.admin_site, using)
        # The user has already confirmed the deletion.
        # Do the deletion and return a None to display the change list view again.
        n = queryset.count()
        print '1'

        try:
            context
        except NameError:
            context = None
        
        print str(context)

        if not context is None:
            print '>> IF'
            for obj in queryset:
                print '4'
                obj_display = force_unicode(obj)
                modeladmin.log_deletion(request, obj, obj_display)
                query = "DELETE FROM events_event WHERE slug='"+str(obj.slug)+"'"
                print query
                from django.db import connections, transaction
                cursor = connections['venezuela'].cursor()
                cursor.execute(query)
                transaction.commit_unless_managed(using='venezuela')
                obj.delete()
    
            modeladmin.message_user(request, _("Successfully deleted %(count)d %(items)s.") % {
                "count": n, "items": model_ngettext(modeladmin.opts, n)
            })
            # Return None to display the change list page again.
            print '2'
            return None
        if len(queryset) == 1:
            objects_name = force_unicode(opts.verbose_name)
        else:
            objects_name = force_unicode(opts.verbose_name_plural)
        if perms_needed or protected:
            title = _("Cannot delete %(name)s") % {"name": objects_name}
        else:
            title = _("Are you sure?")
        print '7'
        context = {
            "title": title,
            "objects_name": objects_name,
            "deletable_objects": [deletable_objects],
            'queryset': queryset,
            "perms_lacking": perms_needed,
            "protected": protected,
            "opts": opts,
            "app_label": app_label,
            'action_checkbox_name': helpers.ACTION_CHECKBOX_NAME,
            'post': 'post',
        }
        # Display the confirmation page
        return TemplateResponse(request, modeladmin.delete_selected_confirmation_template or [
            "admin/%s/%s/delete_selected_confirmation.html" % (app_label, opts.object_name.lower()),
            "admin/%s/delete_selected_confirmation.html" % app_label,
            "admin/delete_selected_confirmation.html"
        ],  context, current_app=modeladmin.admin_site.name)
    really_delete_selected.short_description = _("Delete selected %(verbose_name_plural)s")
    
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

