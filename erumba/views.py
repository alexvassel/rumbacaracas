from decorators import render_to
import datetime
import dateutil.parser
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
@render_to( "erumba/index.html" )
def index(request):
    
    if "submit" in request.POST:
        fdate = request.POST['from_date'].split('.')
        tdate = request.POST['to_date'].split('.')
        from_date = datetime.date(int(fdate[2]),int(fdate[1]),int(fdate[0]))
        to_date   = datetime.date(int(tdate[2]),int(tdate[1]),int(tdate[0]))
    else:
        from_date = datetime.date.today()
        to_date = datetime.date.today() + datetime.timedelta(0)

    return {
        'from_date' : from_date,
        'to_date' : to_date,
    }

@staff_member_required
@render_to( "erumba/setup.html" )
def setup(request):

    from_date = datetime.date.today()
    to_date = from_date
    return {
        'from_date' : from_date,
        'to_date' : to_date,
    }
