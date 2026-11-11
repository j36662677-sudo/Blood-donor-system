
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('add_donor')
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


from django.contrib.auth.forms import AuthenticationForm


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('dashboard_home')
    else:
        form = AuthenticationForm(request)

    return render(request, 'accounts/login.html', {'form': form})

from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('login')