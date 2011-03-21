from locations.models import LocationType, RestaurantType, LocationStyle, LocationMusic, Location, DressType, LocationArea
from django.contrib import admin

class LocationAdmin( admin.ModelAdmin ):
    prepopulated_fields = {"slug": ( "title", )}
    filter_horizontal = ( "type", "restaurant", )
    list_display = ( 'title', 'view', 'style', )
    list_display_links = ( 'title', )
    fieldsets = [
        ( 'Location data', {'fields': ( 
            'title', 'slug', 'type', 'restaurant', 'area', 'dress', 'address', 'city', 'phone_1', 'phone_2',
            'fax', 'url', 'email', 'hours_of_operation',
            'style', 'music', 'resident_dj', 'capacity', 'image_logo', 'description',
        )} ),
        ( 'Contact Information', {'fields': ( 'owner', 'contact_type', 'contact', 'phones', 'contact_email' )} ),
    ]

admin.site.register( Location, LocationAdmin )


admin.site.register( LocationArea )
admin.site.register( LocationType )
admin.site.register( DressType )
admin.site.register( RestaurantType )
admin.site.register( LocationStyle )
admin.site.register( LocationMusic )
