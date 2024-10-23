from rest_framework import serializers
from .models import GeneroModel, AtorModel


class GeneroModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = GeneroModel
        fields = "__all__"


class AtorModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = AtorModel
        fields = ['nome', 'idade']