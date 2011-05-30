from locations.models import LocationType, RestaurantType, LocationMusic, Location, DressType, LocationArea
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


def make_published( modeladmin, request, queryset ):
    queryset.update( status = '1' )
make_published.short_description = _( "Mark selected locations as published" )




class LocationAdmin( admin.ModelAdmin ):
    prepopulated_fields = {"slug": ( "title", )}
    filter_horizontal = ( "type", "restaurant", "days_of_operation" )
    list_display = ( 'title', 'view', 'status' )
    list_display_links = ( 'title', )
    list_filter = ( 'status', )
    fieldsets = [
        ( 'Location data', {'fields': ( 
            'title', 'slug', 'type', 'restaurant', 'area', 'address', 'city', 'district', 'phone_1', 'phone_2',
            'fax', 'url', 'email', 'hours_of_operation', 'days_of_operation',
             'music', 'image_logo', 'description', 'status',
        )} ),
        ( 'Contact Information', {'fields': ( 'owner', 'contact_type', 'contact', 'phones', 'contact_email' )} ),
    ]
    actions = [make_published]

admin.site.register( Location, LocationAdmin )


admin.site.register( LocationArea )
admin.site.register( LocationType )
admin.site.register( DressType )
admin.site.register( RestaurantType )
admin.site.register( LocationMusic )
