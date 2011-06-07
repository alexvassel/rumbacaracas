# Create your views here.

from django.http import HttpResponseRedirect
from django.utils.translation import ugettext as _
from decorators import render_to
from django.forms import ModelForm

from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required

from django import forms

from zinnia.models import Entry
from zinnia.managers import DRAFT

@login_required( login_url = '/login/' )
@render_to( 'news/add.html' )
def add( request ):
    request.breadcrumbs( _( 'News' ) , '/news' )
    request.breadcrumbs( _( 'Add news' ) , request.path_info )

    class EntryForm( ModelForm ):
        #type = ModelMultipleChoiceField( queryset = LocationType.objects.all() )
        #INFO field

        info = forms.CharField( max_length = 100 )

        class Meta:
            model = Entry
            fields = ( 
                'title',
                'info',
                'image',
                'content',
            )
    if request.method == 'POST': # If the form has been submitted...
        form = EntryForm( request.POST, request.FILES ) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            article = form.save( commit = False )
            article.content = article.content + "\n<br /> Info: " + form.cleaned_data['info']
            article.slug = slugify( article.title )
            #set moderation status
            article.status = DRAFT
            article.save()

            article.authors.add( request.user )
            form.save_m2m()
            return HttpResponseRedirect( '/news/' ) # Redirect after POST
        return {
                "form": form,
                "errors": True
        }
    else:
        form = EntryForm()
    return {
        'form': form,
    }
