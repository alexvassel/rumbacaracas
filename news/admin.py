# The admin

from django.contrib import admin

from zinnia.models import Entry
from zinnia.admin import EntryAdmin
from news.models import EntryImage
from django.utils.translation import ugettext_lazy as _


EntryAdmin.fieldsets = ( ( _( 'Content' ), {'fields': ( 'title', 'short' , 'content', 'author', 'source',
                                            'image', 'status' )} ),
                 ( _( 'Options' ), {'fields': ( 'featured', 'show_in_main_slider',
                                            'authors',
                                            'creation_date', 'start_publication',
                                            'end_publication' ),
                                 'classes': ( 'collapse', 'collapse-closed' )} ),
                 ( _( 'Publication' ), {'fields': ( 'categories',
                                                'sites', 'slug' )} ) )
EntryAdmin.list_filter = ( 'categories', 'authors', 'status', 'featured', 'show_in_main_slider',
               'creation_date', 'start_publication',
               'end_publication' )
EntryAdmin.list_display = ( 'get_title', 'get_authors', 'get_categories',
                'get_is_actual', 'get_is_visible', 'get_link', 'status', 'featured', 'show_in_main_slider',
                'creation_date' )
EntryAdmin.list_editable = ( 'status', 'featured', 'show_in_main_slider' )

# Custom Methods

from zinnia.managers import PUBLISHED
from django.utils.html import strip_tags
from django.utils.text import truncate_words
from datetime import datetime

def save_model( self, request, entry, form, change ):
    entry.last_update = datetime.now()
    entry.save()

EntryAdmin.save_model = save_model

class EntryImageInline( admin.TabularInline ):
    model = EntryImage

class EntryAdminImage( EntryAdmin ):
    inlines = ( EntryImageInline, )

admin.site.unregister( Entry )
admin.site.register( Entry, EntryAdminImage )

from news.models import MainSliderPreferences

admin.site.register( MainSliderPreferences )

