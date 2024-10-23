from rest_framework import serializers
from .models import GeneroModel


class GeneroModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = GeneroModel
        fields = "__all__"


