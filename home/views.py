from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from home.forms import RegisterForm, LoginForm
from projects.views import create_modal
from secrets_settings import dados
import html2text
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def home(request):
    return render(request, 'home/home.html')

# @login_required
def profile(request):
    pass
    return HttpResponse()
    # return render()

def settings(request):
    pass
    return HttpResponse()
    # return render()

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


def logout_user(request):
    logout(request)

    return render(request, 'home/home.html')


def contact_me(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    message = request.POST.get('message')

    response = HttpResponse()

    # todo refresh messages
    response['X-IC-Script'] = f'Intercooler.refresh($("#main-content"));'

    try:
        my_email = dados['MY_EMAIL']  # todo check

        print(dados['MY_EMAIL'])
        print(my_email)

        params = {
            'name': name,
            'email': email,
            'message': message,
        }

        html = render_to_string(
            f'extra/contact_email.html',
            params,
        )

        enviado_por = f'"Bruno Organization Web" <{my_email}>'

        email = EmailMultiAlternatives(
            subject=f'Mensagem de {name} - {email}',
            body=html2text.html2text(html),
            from_email=enviado_por,
            to=my_email,
            cc=[],
            bcc=[],

        )

        email.attach_alternative(html, 'text/html')

        email.send()

        messages.success(request, f'Message sended successfully.')
    except:
        messages.error(request, f'Error trying to send message.')

    return response


