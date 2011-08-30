from subscribe.models import User
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext as _
from decorators import render_to
from django.forms import ModelForm
from django.forms import forms
from django.core.urlresolvers import reverse

@render_to( 'subscribe/subscribe.html' )
def subscribe( request ):
    request.breadcrumbs( _( 'Subscription' ) , request.path_info )
    class SubscribeForm( ModelForm ):
        class Meta:
            model = User
            fields = (
                'first_name',
                'last_name',
                'company',
                'sex',
                'birthday',
                'country',
                'city',
                'email',
            )
        def clean_email(self):
            email = self.cleaned_data.get('email')
            try:
                email = User.objects.get(email=email)
            except User.DoesNotExist:
                return email
            except User.MultipleObjectsReturned:
                raise forms.ValidationError(_('This email is already in use.'))
            else:
                raise forms.ValidationError(_('This email is already in use.'))


    if request.method == 'POST' and 'widget_email' not in request.POST: # If the form has been submitted...
        form = SubscribeForm( request.POST ) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            subscribe = form.save()
            return HttpResponseRedirect( reverse('subscribe_done')) # Redirect after POST
        return {
                "form": form,
                "errors": True
        }
    else:
        if 'widget_email' in request.POST:
            data_dict = dict(email= request.POST['widget_email'])
        else:
            data_dict = dict()
            try:
                if request.facebook.uid is not None:
                    data_dict=request.facebook.graph.get_object('me')
            except :
                pass

        form = SubscribeForm(initial= data_dict )
    return {
        'form': form,
    }
