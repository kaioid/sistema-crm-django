from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib import messages


def login(request):
    return render(request, 'login.html')


def submit_login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            django_login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Usuário ou Senha inválido(a). Por favor, tente novamente.')
    return redirect('index')


def logout(request):
    django_logout(request)
    return redirect('login')