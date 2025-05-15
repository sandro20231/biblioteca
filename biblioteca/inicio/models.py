from django.db import models

# Create your models here.


class Autor(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()

    def __str__(self):
        return f"{self.nome} - {self.idade}"


class Livro(models.Model):
    título = models.CharField(max_length=100)
    autor = models.ForeignKey(
        Autor, on_delete=models.CASCADE, related_name="chaveautor")
    resumo = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.titulo} - {self.autor} - {self.resumo}"


class Usuario(models.Model):
    login = models.CharField(max_length=100)
    senha = models.CharField(max_length=10)
