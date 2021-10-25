from django.urls import path, re_path
from django.conf.urls import url
from . import views


urlpatterns = [
    re_path('$', views.CalendarView.as_view(), name='calendar'),

     
    # path('',
    #      views.CalendarView.as_view(),
    #      name='calendar'),
]
