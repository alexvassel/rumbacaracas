from people.models import PhotoEvent, Photo
from django.contrib import admin


class PhotoInline( admin.TabularInline ):
    model = Photo
    readonly_fields = ( 'thumb_tag', )


class EventAdmin( admin.ModelAdmin ):
    list_display = ( 'title', 'category', 'import_photo' )
    inlines = [
        PhotoInline,
    ]

admin.site.register( PhotoEvent, EventAdmin )

