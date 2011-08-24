from django import forms
from django.utils.translation import gettext as _

from django.contrib.auth.models import User

class UserForm(forms.Form):
    username = forms.RegexField(max_length=30, regex=r'^[\w.@+-]+$',
        help_text = _("Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only."),
        error_messages = {'invalid': _("This value may contain only letters, numbers and @/./+/-/_ characters.")})


    email = forms.EmailField(required=False)

    def __init__(self, user, profile, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.user = user
        self.profile = profile

    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        else:
            raise forms.ValidationError(_('This username is already in use.'))

    def save(self, request=None):
        self.user.username = self.cleaned_data.get('username')
        self.user.email = self.cleaned_data.get('email')
        self.user.save()
        self.profile.user = self.user
        self.profile.save()
        return self.user