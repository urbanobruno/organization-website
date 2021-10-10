from django.contrib import admin
from .models import Event
# Register your models here.


class EventAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'day',
        'title',
        'description',
        'start_time',
        'final_time',
    )
    list_display_links = ('id', )
    list_editable = (
        'day',
        'title',
        'start_time',
        'final_time',
    )


admin.register(Event, EventAdmin)
