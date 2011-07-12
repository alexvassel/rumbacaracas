from django.db import models
from preferences.models import Preferences
from django.utils.translation import ugettext_lazy as _
from tinymce import models as tinymce_models

class LastMagazinePreferences( Preferences ):
    __module__ = 'preferences.models'
    anotation = tinymce_models.HTMLField(_('Last Magazine Anotation'))

    class Meta():
        verbose_name = "Last Magazine Anotation"
        verbose_name_plural = "Last Magazine Anotations"
