from django.db import models


class EventCategory( models.Model ):
    title = models.CharField( 'Event Category Title', max_length = 256 )
    def __unicode__( self ):
        return self.title

class DressType( models.Model ):
    title = models.CharField( 'Event Name or Title', max_length = 256 )
    def __unicode__( self ):
        return self.title

class WeekDay( models.Model ):
    value = models.CharField( 'Value', max_length = 256 )
    title = models.CharField( 'Day title', max_length = 256 )
    def __unicode__( self ):
        return self.title


class Event( models.Model ):
    title = models.CharField( 'Event Name or Title', max_length = 256 )
    category = models.ForeignKey( EventCategory )
    from_date = models.DateField( 'Event start date' )
    to_date = models.DateField( 'Event end date' )
    repeat = models.ManyToManyField( WeekDay )
    time = models.TimeField( 'Event time' )
    dress = models.ForeignKey( DressType )
    #local
    place = models.CharField( 'Name of venue / place', max_length = 256 )
    city = models.CharField( 'City', max_length = 256 )
    url = models.URLField( 'Url' )
    email = models.EmailField( 'Email' )
    sort_order = models.IntegerField( 'Hierarchy ' )
    image = models.ImageField( upload_to = 'images/events' )
    image_small = models.ImageField( upload_to = 'images/events' )
    user = models.CharField( 'User', max_length = 256 )
    tuticket_link = models.URLField( 'Link to TuTicket.Com' )
    description = models.TextField( 'Event Description' )
    def __unicode__( self ):
        return self.title
