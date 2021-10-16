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
    print('Chegou View Login')
    def login_user_func(form):
        data = form.cleaned_data
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
        form_model=False,
        submit_button_msg='Login',
        success_msg='Logged successfully',
    )


def register_user(request):
    print('Chegou View Register')

    def create_and_login_user(form):
        # todo check if form clean is being afetuated
        data = form.cleaned_data
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
        form_model=False,
        submit_button_msg='Register',
        success_msg='Registered successfully',
    )


def logout_user(request):
    logout(request)

    return render(request, 'home/home.html')
