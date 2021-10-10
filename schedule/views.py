from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from datetime import datetime, date, timedelta  # todo check date
from django.http import HttpResponse
from calendar import monthrange
from django.views import generic
from .models import Event
from .utils import Calendar


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()


def prev_month(d):
    first = d.replace(day=1)
    month_prev = first - timedelta(days=1)
    month = 'month=' + str(month_prev.year) + '-' + str(month_prev.month)
    return month


def next_month(d):
    days_in_month = monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    month_next = last + timedelta(days=1)
    month = 'month=' + str(month_next.year) + '-' + str(month_next.month)
    return month


# @login_required
class CalendarView(generic.ListView):
    model = Event
    template_name = 'schedule/calendar.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date and month for the calendar
        d = get_date(self.request.GET.get('day', None))
        m = get_date(self.request.GET.get('month', None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        context['calendar'] = cal.formatmonth(withyear=True)

        context['prev_month'] = prev_month(m)
        context['next_month'] = next_month(m)

        return context
