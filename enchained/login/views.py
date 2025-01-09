from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home_page')
    else:
        form = UserCreationForm()
    return render(request, 'login/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home_page')
            else:
                error_message = 'Nom d\'utilisateur ou mot de passe incorrect'
                return render(request, 'login/login.html', {'form': form, 'error_message': error_message})
    else:
        form = LoginForm()

    return render(request, 'login/login.html', {'form': form})
