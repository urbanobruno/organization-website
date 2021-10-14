from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from home.forms import RegisterForm, LoginForm
from projects.views import create_modal


def home(request):
    return render(request, 'home/home.html')


def login_user(request):
    def login_user_func(saved_form):
        data = saved_form.cleaned_data
        user = authenticate(
            request,
            username=data['username'],
            password=data['password'],
        )
        login(request, user)

    return create_modal(
        request,
        LoginForm,
        request.GET.get('url'),
        'Login',
        func_after_form=login_user_func,
        success_msg='Logged successfully',
    )


def register_user(request):
    def create_and_login_user(saved_form):
        # todo check if form clean is being afetuated
        data = saved_form.cleaned_data
        user = User.objects.create(
            username=data['username'],
            email=data['email'],
            password=data['password'],
        )
        login(request, user)

    return create_modal(
        request,
        RegisterForm,
        request.GET.get('url'),
        'Register',
        func_after_form=create_and_login_user,
        success_msg='Registered successfully',
    )


def logout_user(request):
    logout(request)

    return render(request, 'home/home.html')
