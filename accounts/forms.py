from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Account


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Usuário",
        widget=forms.TextInput(
            attrs={"class": "form-control", "style": "color:#dc3545"}
        ),
        error_messages={
            "required": "O nome de usuário é obrigatório.",
            "invalid": "Por favor, insira um nome de usuário válido.",
        },
    )
    password = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "style": "color:#dc3545"}
        ),
        error_messages={
            "required": "A senha é obrigatória.",
        },
    )


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        label="Usuário",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        error_messages={
            "required": "O nome de usuário é obrigatório.",
            "invalid": "Por favor, insira um nome de usuário válido.",
        },
    )
    password1 = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        error_messages={
            "required": "A senha é obrigatória.",
        },
    )
    password2 = forms.CharField(
        label="Confirme a Senha",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        error_messages={
            "required": "A confirmação da senha é obrigatória.",
            "invalid": "As senhas não coincidem.",
        },
    )
    email = forms.CharField(
        label="E-mail",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        error_messages={
            "required": "O e-mail é obrigatório.",
            "invalid": "Por favor, insira um e-mail válido.",
        },
    )

    class Meta:
        model = Account
        fields = ("username", "email", "password1", "password2")
        labels = {
            "username": "Usuário",
            "email": "E-mail",
            "password1": "Senha",
            "password2": "Confirme a Senha",
        }
