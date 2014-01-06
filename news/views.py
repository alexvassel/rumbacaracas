# Create your views here.

from django.http import HttpResponseRedirect
from django.utils.translation import ugettext as _
from decorators import render_to
from django.forms import ModelForm

from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required

from django import forms

from zinnia.models import Entry
from news.models import EntryImage
from zinnia.managers import DRAFT
from django.utils.html import strip_tags
from locations.templatetags.tools import truncate
from django.forms.models import inlineformset_factory
from main.modelFields import SlugifyUniquely
from django.core.urlresolvers import reverse

#Add to a form containing a FileField and change the field names accordingly.
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from zinniaModels import AuthorProfile
from django.contrib.auth.models import User
from django.core.paginator import Paginator, InvalidPage, EmptyPage

@login_required( login_url = '/login/' )
@render_to( 'news/add.html' )
def add( request, type ):
    request.breadcrumbs( _( 'News' ) , reverse('zinnia_entry_archive_index'))

    if type == 'blog':
        request.breadcrumbs( _( 'Add Article' ) , request.path_info )
    else :
        request.breadcrumbs( _( 'Add News' ) , request.path_info )

    EntryImageFormSet = inlineformset_factory( 
        Entry,
        EntryImage,
        extra = 5,
        can_delete = False
     )


    class EntryForm( ModelForm ):
#        def clean_content(self):
#            image = self.cleaned_data['image']
#            content_type = content.content_type
#            if content_type in settings.IMAGE_CONTENT_TYPES:
#                if content._size > settings.IMAGE_MAX_UPLOAD_SIZE:
#                    raise forms.ValidationError(_('Please keep filesize under %(maxsize)s. Current filesize %(current)s') % dict(maxsize=filesizeformat(settings.IMAGE_MAX_UPLOAD_SIZE), current=filesizeformat(content._size)))
#            else:
#                raise forms.ValidationError(_('File type is not supported'))
#            return image

        class Meta:
            model = Entry
            fields = ( 
                'title',
                'source', 
                'author',
                'image',
                'content',
            )
    if request.method == 'POST': # If the form has been submitted...
        form = EntryForm( request.POST, request.FILES ) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            article = form.save( commit = False )
            article.short = truncate( strip_tags( article.content ), 100 )
            article.content = strip_tags( article.content )
            article.slug = SlugifyUniquely( article.title, article.__class__)
            #set moderation status
            article.status = DRAFT
            #article.save()
            images_formset = EntryImageFormSet( request.POST, request.FILES, instance = article )
            if images_formset.is_valid():
                article.save()
                images_formset.save()

            article.authors.add( request.user )
            form.save()
            for field in form:
                print 'Field: '
                print field

            return {
                    "completed": True,
                "form": form,
                "type": type,
                "errors": True
        }#HttpResponseRedirect( reverse('zinnia_entry_archive_index') ) # Redirect after POST
        else :
            images_formset = EntryImageFormSet( instance = Entry() )

        return {
                "form": form,
                "type": type,
                'imagesForm': images_formset,
                "errors": True
        }
    else:
        form = EntryForm()
        images_formset = EntryImageFormSet( instance = Entry() )
    return {
        'form': form,
        "type": type,
        'imagesForm': images_formset,
    }


@render_to( 'news/profile_detail.html' )
def ath_profile ( request,profile_id):
    dict = {}
    try:
        profileid = User.objects.filter(username=profile_id)
        profile = AuthorProfile.objects.select_related('user').filter(user=profileid[0].id)
        entries = Entry.objects.filter(author_profile=profile[0])
    except Exception:
        profileid = None
        profile = None
        entries = None
    try:
        page = int( request.GET.get( 'page', '1' ) )
    except ValueError:
        page = 1
 
    if entries:
        paginator = Paginator( entries, 12 )
        try:
            locations_page = paginator.page( page )
        except ( EmptyPage, InvalidPage ):
            locations_page = paginator.page( paginator.num_pages )
    else:
            locations_page = None
            paginator = None
    entries = Entry.published.filter(authors=profileid[0].id)[1:6]
    dict['profile']=profile
    dict['entry']=locations_page
    dict['current_page']=locations_page
    dict['current_paginator']=paginator
    return dict


