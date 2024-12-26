from rest_framework import serializers
from django.db.models import Avg, Sum
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
    media_avaliacao = serializers.SerializerMethodField(read_only=True)
    soma_avaliacao = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Filme
        fields = '__all__'

    def get_media_avaliacao(self, instance):
        media_de_avaliacao = instance.avaliacoes.aggregate(valor_medio=Avg('estrelas'))['valor_medio']

        if media_de_avaliacao:
            return media_de_avaliacao

        return "Filme sem avaliação"

    def get_soma_avaliacao(self, instance):
        soma_avaliacao = instance.avaliacoes.aggregate(valor_total=Sum("estrelas"))[
            "valor_total"
        ]

        if soma_avaliacao:
            return soma_avaliacao
        
        return 0

    def validate(self, instance):
        print(instance)
        movie_year = instance["ano_de_lancamento"]
        actors = instance["atores"]
        for actor in actors:
            actor_year = actor.data_de_nascimento.year

            if actor_year >= movie_year:
                raise serializers.ValidationError(
                    f"Não é possível ator {actor.nome} com a data de nascimento ({actor_year}) no ano de lançamento do filme ({movie_year})."
                )
        return instance


"""
    def validate(self, dados):
        ano_lancamento = dados['ano_de_lancamento']
        atores = dados['atores']

        for ator in atores:
            data_nascimento_ator = ator.data_de_nascimento
            ano_de_nascimento = data_nascimento_ator.year
            if ano_de_nascimento < 1995 or ano_lancamento < 1995:
                raise serializers.ValidationError(f"O ano de nascimento do ator {ator.nome}é inferior a 1995 ou o filme é menor que 1995")
            
        return dados
"""

'''
    def validate_ano_de_lancamento(self, value):
        if value < 2000:
            raise serializers.ValidationError("Daqui você não passa, tem que ser um ano maior que 2000")
        return value
'''
