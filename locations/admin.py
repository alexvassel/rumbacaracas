from locations.models import LocationType, RestaurantType, LocationMusic, Location, DressType, LocationArea
from news.zinniaModels import AuthorProfile
from django.contrib.auth.models import User
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


def make_published( modeladmin, request, queryset ):
    queryset.update( status = '1' )
make_published.short_description = _( "Mark selected locations as published" )



class LocationTypeAdmin( admin.ModelAdmin ):
    prepopulated_fields = {"slug": ( "title", )}
    list_display = ( 'title', 'slug','fb_type', 'show_in_menu', )
    list_editable = ( 'show_in_menu', )
admin.site.register( LocationType, LocationTypeAdmin )



class LocationAdmin( admin.ModelAdmin ):
    prepopulated_fields = {"slug": ( "title", )}
    search_fields = ['title']
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
#new model register for author
class ProfileAdmin( admin.ModelAdmin ):
    list_display = ( 'user', 'profile_photo','about_author','view_profile' )
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":
            kwargs["queryset"] = User.objects.filter(is_staff=True)
        return super(ProfileAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
    def view_profile(self, obj):
        usernames=User.objects.filter(id=obj.user_id)
        return u"<a href='%s%s' target='_blank'>view profile</a>" %("/locales/profile/",usernames[0].username)
    view_profile.allow_html = True
    view_profile.allow_tags = True  
    view_profile.short_description = 'Action'
admin.site.register( AuthorProfile, ProfileAdmin )