from django.urls import path
from . import views

urlpatterns = [
    path('',
         views.home,
         name='home'),
    path('profile',
         views.profile,
         name='profile'),
    path('settings',
         views.settings,
         name='settings'),
    path('reset_password',
         views.reset_password,
         name='reset_password'),
    path('login_user',
         views.login_user,
         name='login_user'),
    path('register_user',
         views.register_user,
         name='register_user'),
    path('logout_user',
         views.logout_user,
         name='logout_user'),
    path('contact_me',
         views.contact_me,
         name='contact_me'),
]
