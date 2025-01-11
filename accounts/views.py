from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.checks import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')  # Замените 'home' на имя вашей главной страницы
    else:
        form = AuthenticationForm()
    return render(request, 'login.html')


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Перенаправляем на страницу входа
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')
