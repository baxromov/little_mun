from django.shortcuts import render, redirect
from users.forms.users import RegisterForm
from users.models import User
from django.contrib import messages


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
            return redirect('/')
        else:
            messages.add_message(request, messages.INFO, f'{form.errors}')
            return render(request, 'auth/registration.html')
    return render(request, 'auth/registration.html')
