from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class LoginForm(forms.BaseForm):
    username = forms.CharField(required=True)
    password = forms.PasswordInput()

    def clean(self):
        data = self.data
        user = User.objects.filter(username=data['username'])
        if not user.exists():
            self.add_error(
                'username',
                'User with this username does not exists.'
            )
        elif user.password != data['password']:
            self.add_error(
                'password',
                'Password is incorrect.'
            )


class RegisterForm(forms.BaseForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password = forms.PasswordInput()
    check_password = forms.PasswordInput()

    def clean(self):
        data = self.data
        if User.objects.filter(username=data['username']).exists():
            self.add_error(
                'username',
                'User with this username alredy exists.'
            )
        if User.objects.filter(email=data['email']).exists():
            self.add_error(
                'email',
                'User with this email alredy exists.'
            )
        if len(data['password']) < 6:
            self.add_error(
                'password',
                'Password must be at least 6 characters long.'
            )
        if data['password'] != data['check_password']:
            self.add_error(
                'check_password',
                'Passwords are not the same.'
            )

