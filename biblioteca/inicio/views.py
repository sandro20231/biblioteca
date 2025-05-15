from django.shortcuts import render
from .models import Autor, Livro, Usuario
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.


def login_a(request):
    if request.method == "POST":
        username = request.POST['tlogin']
        password = request.POST['tsenha']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        return render(request, 'inicio/erro.html', {"mensagem": "Não foi possível fazer o login"})
    return render(request, "inicio/login.html")


def logout_a(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


def index(request):
    return render(request, 'inicio/index.html')


def erro(request):
    return render(request, 'inicio/erro.html')


def inicio(request):
    return render(request, "inicio/inicio.html")
