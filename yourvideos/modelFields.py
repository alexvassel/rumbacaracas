from django.db import models
import re

class YoutubeField( models.CharField ):
    '''
    transparently check if it a link and parse id
    '''
    def get_db_prep_save( self, value ):
        if value is not None:
            regex = re.compile( r"^(http://)?(www\.)?(youtube\.com/watch\?v=)?(?P<id>[A-Za-z0-9\-=_]{11})" )
            match = regex.match( value )
            if match:
                value = match.group( 'id' )
        return models.CharField.get_db_prep_save( self, value )
