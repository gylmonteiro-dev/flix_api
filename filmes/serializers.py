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
        filme = Filme.objects.create(**validated_data)
        filme.atores.set(todos_os_atores)
        return filme
    
    # Não iremos utilizar o serializador manual. Por enquanto



class  FilmeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filme
        fields = "__all__"

    def validate_ano_de_lancamento(self, value):
        if value < 2000:
            raise serializers.ValidationError("Daqui você não passa, tem que ser um ano maior que 2000")
        return value
    
    def validate(self, dataset):
        print(dataset)
        ano_lancamento_filme = dataset['ano_de_lancamento']
        # atores = dataset['atores']
        


        # if ano_lancamento_filme < 1995 and atores.data_de_nascimento < 1995:
            # raise serializers.ValidationError("Nem atores nem filmes podem ser anteriores a 1995")
        return dataset


