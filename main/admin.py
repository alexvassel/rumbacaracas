from django.contrib import admin
from sortable.admin import SortableAdmin
from main.models import Place, MainBackgroundImage, CursorImage, SplashScreen


class PlaceAdmin( SortableAdmin ):
    list_editable = SortableAdmin.list_editable + ( 'background_image', 'cursor_image', 'splash_image' )
    list_display = SortableAdmin.list_display + ( 'title', 'background_image', 'cursor_image', 'splash_image' )
    list_display_links = ( 'title', )


class SplashScreenAdmin(admin.ModelAdmin):
    #def has_change_permission(self, request, obj):
        #return obj is None or self.queryset(request).filter(pk=obj.pk).count() > 0
    #    return True
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register( Place, PlaceAdmin )
admin.site.register( MainBackgroundImage )
admin.site.register( CursorImage )
admin.site.register( SplashScreen, SplashScreenAdmin )

