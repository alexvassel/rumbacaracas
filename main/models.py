from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db import models
from django.utils.translation import ugettext_lazy as _

SEX_STATUSES = (
    ( 'male', _( 'Male' ) ),
    ( 'female', _( 'Female' ) ),
 )


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    sex = models.CharField( max_length = 64, choices = SEX_STATUSES, blank=True )
    birthday = models.DateField(_('Date of birth'), blank=True, null=True)
    subscribed = models.BooleanField(_('User subscribed to erumba'), default=False)

    def __str__(self):
          return "%s's profile" % self.user

def create_user_profile(sender, instance, created, **kwargs):
    if created:
       profile, created = UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)


from socialregistration import signals
from socialregistration import models

def connect_facebook(user, profile, client, **kwargs):
    #data_dict=request.facebook.graph.get_object('me')

    #gender = profile["gender"]
    #dateofbirth = profile["birthday"]
    # Do fancy stuff like fetching more user info with the client
    pass

signals.connect.connect(connect_facebook, sender = models.FacebookProfile)
