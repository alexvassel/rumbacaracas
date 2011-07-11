from django import template
register = template.Library()

from events.models import Event 
from yourphotos.models import Photo

import calendar
from datetime import datetime, timedelta, time




@register.inclusion_tag( 'widgets/magazine.html' )
def magazine_block( ):
    return dict()

@register.inclusion_tag( 'widgets/subscribe.html' )
def subscribe_block( ):
    return dict()


@register.inclusion_tag( 'widgets/yourphotos.html' )
def yourphotos_block( ):
    photos = Photo.objects.filter(status=1).order_by('-datetime_added')[:4]
    return dict(photos=photos)


def get_last_day_of_month(year, month):
    if (month == 12):
        year += 1
        month = 1
    else:
        month += 1
    return date(year, month, 1) - timedelta(1)

def month_cal(year=None, month=None):

    today = datetime.today()

    if year is None:
        year = today.year
    if month is None:
        month = today.month

    calendar.setfirstweekday( 6 )
    dtstart = datetime( year, month, 1 )
    last_day = calendar.monthrange( year, month )[1]
    dtend = datetime( year, month, last_day )

    event_list = Event.objects.get_occuriences(start_date=dtstart, end_date=dtend)
    events_dates = [dt for event, dt in event_list]

    first_day_of_month = dtstart.date()
    last_day_of_month = dtend.date()
    
    first_day_of_calendar = first_day_of_month - timedelta(first_day_of_month.weekday())
    last_day_of_calendar = last_day_of_month + timedelta(7 - last_day_of_month.weekday())




    month_cal = []
    week = []
    week_headers = []

    i = 0
    day = first_day_of_calendar
    while day <= last_day_of_calendar:
        if i < 7:
            week_headers.append(day)
        cal_day = {}
        cal_day['day'] = day
        cal_day['event'] = False
        cal_day['in_month'] = False

        if day in events_dates:
            cal_day['event'] = True

        if day.month == month:
            cal_day['in_month'] = True

        week.append(cal_day)
        if day.weekday() == 6:
            month_cal.append(week)
            week = []
        i += 1
        day += timedelta(1)

    return {'calendar': month_cal, 'headers': week_headers, 'first_day_of_month': first_day_of_month }

register.inclusion_tag('widgets/calendar.html')(month_cal)