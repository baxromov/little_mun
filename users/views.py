from django.shortcuts import render, redirect
from users.forms.users import RegisterForm
from users.forms.auth import LoginForm
from users.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']

            User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password1
            )
            auth_user = authenticate(request, username=username, password=password1)
            login(request, auth_user)
            return redirect('/')
        else:
            messages.add_message(request, messages.INFO, f'{form.errors}')
            return render(request, 'auth/registration.html')
    return render(request, 'auth/registration.html')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.add_message(request, messages.INFO, f"User is not found: {username} {password}")
    return render(request, 'auth/login.html')


def logout_view(request):
    logout(request)
    return redirect('/')
