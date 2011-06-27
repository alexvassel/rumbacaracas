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




@login_required( login_url = '/login/' )
@render_to( 'news/add.html' )
def add( request, type ):
    request.breadcrumbs( _( 'News' ) , '/news' )

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
            article.slug = slugify( article.title )
            #set moderation status
            article.status = DRAFT
            #article.save()
            images_formset = EntryImageFormSet( request.POST, request.FILES, instance = article )
            if images_formset.is_valid():
                article.save()
                images_formset.save()

            article.authors.add( request.user )
            form.save_m2m()

            return HttpResponseRedirect( '/news/' ) # Redirect after POST
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
