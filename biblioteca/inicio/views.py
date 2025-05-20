from django.shortcuts import render
from .models import Autor, Livro, Usuario
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework import viewsets
from .models import Autor, Livro
from .serializers import AutorSerializer, LivroSerializer

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


def novoautor(request):
    if request.method == "POST":
        nome = request.POST['nanome']
        idade = request.POST['naidade']

        registro = Autor(nome=nome, idade=idade)
        registro.save()
        return HttpResponseRedirect(reverse('listaautor'))

    return render(request, 'inicio/novoautor.html')


def listaautor(request):
    registros = Autor.objects.all()
    return render(request, 'inicio/listaautor.html', {"registros": registros})


def exibirautor(request, id):
    registro = Autor.objects.get(pk=id)
    return render(request, 'inicio/exibirautor.html', {"registro": registro})


def buscarautoradeletar(request):
    if request.method == "POST":
        id = request.POST['idexcluir']
        registro = Autor.objects.get(pk=id)
        return render(request, 'inicio/deletarautor.html', {"registro": registro})
    return render(request, 'inicio/deletarautor.html')


def excluirautor(request):
    if request.method == "POST":
        id = request.POST['idex']
        registro = Autor.objects.get(pk=id)
        registro.delete()
        return HttpResponseRedirect(reverse('listaautor'))


def busc(request):
    if request.method == "POST":
        id = request.POST['idalterar']
        registro = Autor.objects.get(pk=id)
        return render(request, 'inicio/alterarautor.html', {"registro": registro})
    return render(request, 'inicio/alterarautor.html')


def alterarautor(request):
    if request.method == "POST":
        id = request.POST['id2alterar']
        nome = request.POST['novonome']
        idade = request.POST['novaidade']

        registro = Autor.objects.get(pk=id)
        registro.nome = nome
        registro.idade = idade
        registro.save()
        return HttpResponseRedirect(reverse('listaautor'))


def novolivro(request):
    if request.method == "POST":
        titulo = request.POST['titulolivro']
        autor = request.POST['autorlivro']
        registroautor = Autor.objects.filter(nome=autor).first()
        resumo = request.POST['resumolivro']

        registrolivro = Livro(
            título=titulo, autor=registroautor, resumo=resumo)
        registrolivro.save()
        return HttpResponseRedirect(reverse('todoslivros'))
    return render(request, 'inicio/novolivro.html')


def todoslivros(request):
    registros = Livro.objects.all()
    return render(request, 'inicio/todoslivros.html', {"registros": registros})


def buscadeletar(request):
    if request.method == "POST":
        id = request.POST['idexcluir3']
        registro = Livro.objects.get(pk=id)
        return render(request, 'inicio/excluirlivro.html', {"registro": registro})
    return render(request, 'inicio/excluirlivro.html')


def deletarlivro(request):
    if request.method == "POST":
        id = request.POST['idexcluir4']
        registro = Livro.objects.get(pk=id)
        registro.delete()
        return HttpResponseRedirect(reverse('todoslivros'))


class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer


def listarlivrosapi(request):
    return render(request, 'inicio/ca_listandolivros.html')


def listarautoresapi(request):
    return render(request, 'inicio/ca_listandoautores.html')


def salvarautor(request):
    return render(request, 'inicio/ca_salvarautor.html')


def salvarlivro(request):
    return render(request, 'inicio/csa_salvarlivro.html')
