from subscribe.models import Users
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext as _
from decorators import render_to
from django.forms import ModelForm
from django.forms import forms


@render_to( 'subscribe/subscribe.html' )
def subscribe( request ):
    request.breadcrumbs( _( 'Subscription' ) , request.path_info )
    class SubscribeForm( ModelForm ):
        class Meta:
            model = Users
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
                email = Users.objects.get(email=email)
            except Users.DoesNotExist:
                return email
            except Users.MultipleObjectsReturned:
                raise forms.ValidationError(_('This email is already in use.'))
            else:
                raise forms.ValidationError(_('This email is already in use.'))

    if request.method == 'POST': # If the form has been submitted...
        form = SubscribeForm( request.POST ) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            subscribe = form.save()
            return HttpResponseRedirect( '/subscribe/done' ) # Redirect after POST
        return {
                "form": form,
                "errors": True
        }
    else:
        if request.facebook.uid is not None:
            data_dict=request.facebook.graph.get_object('me')
        form = SubscribeForm(data_dict)
    return {
        'form': form,
    }
