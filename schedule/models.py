from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from calendar import HTMLCalendar

# Create your models here.


class Event(models.Model):
    day = models.DateField(verbose_name='Day of the event')
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True, verbose_name='Starting Time')
    final_time = models.TimeField(null=True, blank=True, verbose_name='Final Time')

    def clean(self):
        if self.final_time < self.start_time:
            raise ValidationError({
                'final_time': 'Ending day must be after starting day'
            })
