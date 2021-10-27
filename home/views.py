from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.views.decorators.http import require_POST
from home.forms import RegisterForm, LoginForm
from projects.views import create_modal
from secrets_settings import dados
from django.core.mail import send_mail


def home(request):
    return render(request, 'home/home.html')


# @login_required
def profile(request):
    pass
    return HttpResponse()
    # return render()


# @login_required
def settings(request):
    pass
    return HttpResponse()
    # return render()


# @login_required
def reset_password(request):
    pass
    return HttpResponse()
    # return render()


def login_user(request):
    print('Chegou View Login')

    def login_user_func(form):
        data = form.cleaned_data
        user = authenticate(
            request,
            username=data['username'],
            password=data['password'],
        )
        if user is not None:
            login(request, user)
        form.add_error('username', 'user invalid.')
        form.add_error('password', 'user invalid.')

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


# @login_required
def logout_user(request):
    logout(request)

    return render(request, 'home/home.html')


@require_POST
def contact_me(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    message = request.POST.get('message')

    try:
        my_email = dados['EMAIL_WEB']  # todo check

        message_email = f"""
        Mensagem de Organization Web \n
        \n
        Nome: {name} \n
        Email: {email} \n
        Mensagem: \n
        {message}
        
        """

        send_mail(
            subject=f'Mensagem Organização Web de {name} - {email}',
            message=message_email,
            from_email=my_email,
            recipient_list=[my_email, dados['MY_EMAIL']],
        )
    except Exception as e:
        # todo implement system to send all exceptions
        messages.error(request, f'Error trying to send message.')

    return render(request, 'home/home.html')
