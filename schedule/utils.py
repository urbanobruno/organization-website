from calendar import HTMLCalendar
from datetime import datetime, timedelta
from .models import Event


class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()

    # formats a day as a td
    # filter events by day
    def formatday(self, day, events):
        events_filter_day = events.filter(day__day=day)
        # list_events_day = ''.join([f'<li> {e.title} <li>' for e in events_filter_day])
        # todo
        list_events_day = ''

        for event in events_filter_day:
            list_events_day += f'<li> {event.title} </li>'


        # todo implementar id e colocar funcao intercooler que chama view
        if day != 0:
            return f"<td><span class='date'>{day}</span><ul> {list_events_day} </ul></td>"
        return '<td></td>'

    # formats a week as a tr
    def formatweek(self, theweek, events):
        print(theweek)
        week = ''
        for day, weekday in theweek:
            week += self.formatday(day, events)
        return f'<tr> {week} </tr>'

    # formats a month as a table
    # filter events by year and month
    def formatmonth(self, withyear=True):
        events = Event.objects.filter(day__year=self.year, day__month=self.month)

        calendar = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        calendar += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        calendar += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            calendar += f'{self.formatweek(week, events)}\n'
        return calendar
