from django.db import models
from django.utils.translation import ugettext_lazy as _

USER_STATUSES = (
    ( '1', _( 'Subscribed' ) ),
    ( '2', _( 'Unsubcribed' ) ),
 )

SEX_STATUSES = (
    ( 'male', _( 'Male' ) ),
    ( 'female', _( 'Female' ) ),
 )


class User( models.Model ):
    first_name = models.CharField(_('First name'), max_length = 256)
    last_name = models.CharField(_('Last name'), max_length = 256)
    company = models.CharField(_('Company'), max_length = 256, blank = True)
    sex = models.CharField(_('Sex'), choices = SEX_STATUSES, max_length = 64)
    birthday = models.DateField(_('Birthday date'))
    country = models.CharField(_('Country'), max_length = 64, blank = True)
    city = models.CharField(_('City'), max_length = 64, blank = True)
    email = models.EmailField(_('Email'))
    status = models.CharField(_('Subscribe status'), choices = USER_STATUSES, default = 1, max_length = 64 )

    def __unicode__( self ):
        return "%s %s" % (self.last_name, self.first_name)

    class Meta:
        verbose_name = _( 'Subscribed User' )
        verbose_name_plural = _( 'Subscribed Users' )
