from rest_framework import serializers
from .models import Autor, Livro


class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'


class LivroSerializer(serializers.ModelSerializer):
    autor_nome = serializers.StringRelatedField(source='autor', read_only=True)

    class Meta:
        model = Livro
        fields = ['id', 'título', 'resumo', 'autor', 'autor_nome']
