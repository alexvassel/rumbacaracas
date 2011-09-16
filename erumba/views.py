from decorators import render_to
import datetime
import dateutil.parser


@render_to( "erumba/index.html" )
def index(request):

    from_date = datetime.date.today()
    to_date = datetime.date.today() + datetime.timedelta(6)
    return {
        'from_date' : from_date,
        'to_date' : to_date,
    }
