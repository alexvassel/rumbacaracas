from locations.models import LocationType, RestaurantType, LocationMusic, Location, DressType, LocationArea
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


def make_published( modeladmin, request, queryset ):
    queryset.update( status = '1' )
make_published.short_description = _( "Mark selected locations as published" )



class LocationTypeAdmin( admin.ModelAdmin ):
    prepopulated_fields = {"slug": ( "title", )}
    list_display = ( 'title', 'slug', 'show_in_menu', )
    list_editable = ( 'show_in_menu', )
admin.site.register( LocationType, LocationTypeAdmin )



class LocationAdmin( admin.ModelAdmin ):
    prepopulated_fields = {"slug": ( "title", )}
    filter_horizontal = ( "type", "restaurant", "days_of_operation" )
    list_display = ( 'title', 'view', 'status' , 'featured', )
    list_editable = ( 'status', 'featured' )
    list_display_links = ( 'title', )
    list_filter = ( 'status', 'featured' )
    readonly_fields = ( 'add_user', )
    fieldsets = [
        ( 'Location data', {'fields': ( 
            'title', 'slug', 'type', 'restaurant', 'area', 'address', 'city', 'phone_1', 'phone_2',
            'fax', 'url', 'email', 'hours_of_operation', 'days_of_operation',
             'music', 'image_logo', 'description', 'status', 'featured',
             'add_user',
        )} ),
        ( 'Contact Information', {'fields': ( 'owner', 'contact_type', 'contact', 'phones', 'contact_email' )} ),
    ]
    actions = [make_published]

admin.site.register( Location, LocationAdmin )


admin.site.register( LocationArea )
admin.site.register( DressType )
admin.site.register( RestaurantType )
admin.site.register( LocationMusic )
