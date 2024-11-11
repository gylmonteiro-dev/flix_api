from rest_framework import serializers
from .models import Filme
from generos.models import GeneroModel
from atores.models import Ator

class FilmeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    titulo = serializers.CharField()
    genero = serializers.PrimaryKeyRelatedField(queryset=GeneroModel.objects.all())
    ano_de_lancamento = serializers.IntegerField()
    atores = serializers.PrimaryKeyRelatedField(queryset=Ator.objects.all(), many=True)
    resumo = serializers.CharField()
    
    def create(self, validated_data):
        todos_os_atores = validated_data.pop("atores")
        print(todos_os_atores)
        filme = Filme.objects.create(**validated_data)
        filme.atores.set(todos_os_atores)
        return filme



class  FilmeModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Filme
        fields = "__all__"

