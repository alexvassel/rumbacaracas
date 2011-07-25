# The admin

from django.contrib import admin

from zinnia.models import Entry
from zinnia.admin import EntryAdmin
from news.models import EntryImage
from django.utils.translation import ugettext_lazy as _

#
EntryAdmin.fieldsets = ( ( _( 'Content' ), {'fields': ( 'title', 'short' , 'content', 'author', 'source',
                                            'image','slider_image', 'status' )} ),
                 ( _( 'Options' ), {'fields': ( 'show_in_main_slider',
                                            'authors',
                                            'creation_date', 'start_publication',
                                            'end_publication' ),
                                 'classes': ( 'collapse', 'collapse-closed' )} ),
                 ( _( 'Publication' ), {'fields': ( 'categories',
                                                'sites', 'slug' )} ) )
EntryAdmin.list_filter = ( 'categories', 'status','show_in_main_slider',
               'creation_date', 'start_publication',
               'end_publication' )
EntryAdmin.list_display = ( 'get_title', 'get_categories',
                'get_is_actual', 'get_is_visible', 'get_link', 'status', 'show_in_main_slider',
                'creation_date' )
EntryAdmin.list_editable = ( 'status', 'show_in_main_slider' )

# Custom Methods

from zinnia.managers import PUBLISHED
from django.utils.html import strip_tags
from django.utils.text import truncate_words
from datetime import datetime

class EntryImageInline( admin.TabularInline ):
    model = EntryImage

class EntryAdminImage( EntryAdmin ):
    inlines = ( EntryImageInline, )
    search_fields = ['title']
    def save_model( self, request, entry, form, change ):
        entry.last_update = datetime.now()
        entry.save()

    def get_title(self, entry):
        """Return the title with word count and number of comments"""
        title = _('%(title)s (%(word_count)i words)') % \
                {'title': entry.title, 'word_count': entry.word_count}
        return title
    get_title.short_description = _('title')
    

admin.site.unregister( Entry )
admin.site.register( Entry, EntryAdminImage )

from news.models import MainSliderPreferences

admin.site.register( MainSliderPreferences )

