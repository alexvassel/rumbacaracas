from django.contrib import admin
from sortable.admin import SortableAdmin
from main.models import Place, MainBackgroundImage, CursorImage


class PlaceAdmin( SortableAdmin ):
    list_editable = SortableAdmin.list_editable + ( 'background_image', 'cursor_image', )
    list_display = SortableAdmin.list_display + ( 'title','background_image','cursor_image',)
    list_display_links = ( 'title', )


admin.site.register( Place, PlaceAdmin )
admin.site.register( MainBackgroundImage )
admin.site.register( CursorImage )


