from subscribe.models import  User
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

def make_unsubscribed( modeladmin, request, queryset ):
    queryset.update( status = '2' )
make_unsubscribed.short_description = _( "Mark selected users as unsubscribed" )


class SubscribeAdmin( admin.ModelAdmin ):
    list_filter = ( 'status', )
    actions = [make_unsubscribed]

admin.site.register( User, SubscribeAdmin )
