# The admin

from django.contrib import admin

from zinnia.models import Entry
from zinnia.admin import EntryAdmin
from news.models import EntryImage
from django.utils.translation import ugettext_lazy as _
from zinniaModels import AuthorProfile
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

#MONKEY PATCHING OF ZINNIA ADMIN
EntryAdmin.fieldsets = ( ( _('Content'), {'fields': ( 'title', 'short', 'content', 'authors',

                                                      'image', 'slider_image', 'status' )} ),
#                         ( _('Image preview'), {'fields': ('preview_as_image', 'preview_image' )} ),
                         ( _('Options'), {'fields': ( 'show_in_main_slider',
                                                      'creation_date', 'start_publication',
                                                      'end_publication' ),
                                          'classes': ( 'collapse', 'collapse-closed' )} ),
                         ( _('Publication'), {'fields': ( 'categories',
                                                          'sites', 'slug' )} ) )
EntryAdmin.list_filter = ( 'categories', 'status','show_in_main_slider',
               'creation_date', 'start_publication',
               'end_publication' )
EntryAdmin.list_display = ( 'get_title', 'get_categories',
                'get_is_actual', 'get_is_visible', 'get_link', 'status', 'show_in_main_slider',
                'creation_date' )
EntryAdmin.list_editable = ( 'status', 'show_in_main_slider' )


EntryAdmin.actions = [ 'make_published', 'make_hidden','make_tweet', 'put_on_top']


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

#new model register for author
class ProfileAdmin( admin.ModelAdmin ):
    list_display = ( 'user', 'profile_photo','about_author','view_profile' )
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":
            kwargs["queryset"] = User.objects.filter(is_staff=True)
        return super(ProfileAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
    def view_profile(self, obj):
        usernames=User.objects.filter(id=obj.user_id)
        return u'<a href="%s" target="_blank">%s</a>' % ( reverse('ath_profile', None, kwargs={'profile_id':usernames[0].username} ), _( 'View Profile' ) )
#        return u"<a href='%s%s' target='_blank'>view profile</a>" %("/locales/profile/",usernames[0].username)
    view_profile.allow_html = True
    view_profile.allow_tags = True  
    view_profile.short_description = 'Action'
admin.site.register( AuthorProfile, ProfileAdmin )
