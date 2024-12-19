from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import (
    login_required,
    permission_required,
    user_passes_test,
)

# Create your views here.


def staff_required(user):
    return user.is_authenticated and user.is_staff


def user_login_required(user):
    return user.is_authenticated


def is_user(user):
    return not user.is_staff


def user_signup(request):
    if request.user.is_authenticated:
        return redirect("/")
    msg = None
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = "user created"
            return redirect("/accounts/usersignin")
        else:
            msg = "form is not valid"
    else:
        form = SignUpForm()
    return render(request, "user_register.html", {"form": form, "msg": msg})


def user_login(request):
    if request.user.is_authenticated:
        return redirect("/")
    return login_view(request)


def admin_login(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect("/admin")
    return login_view(request)


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Redireciona para 'index' ao invés de 'consulta'
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')


@user_passes_test(staff_required, login_url="/adminlogin")
def admin(request):
    return render(request, "admin.html")


@login_required(login_url="/login")
def customer(request):
    return render(request, "customer.html")


def signout(request):
    if request.user.is_staff:
        url = "/admin"
    else:
        url = "/"
    logout(request)
    return redirect(url)
