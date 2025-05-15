from django.shortcuts import render
from .models import Autor, Livro, Usuario
# Create your views here.


def teste(request):
    return render(request, "inicio/layout.html")
