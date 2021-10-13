from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home/home.html')


def login_user(request):
    pass


def register_user(request):
    pass


def logout_user(request):
    logout(request)

    return render(request, 'home/home.html')

