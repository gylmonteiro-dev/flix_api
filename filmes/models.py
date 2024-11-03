from django.db import models
from generos.models import GeneroModel
from atores.models import Ator
# Create your models here.


class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    genero = models.ForeignKey(GeneroModel, on_delete=models.PROTECT, related_name='filmes')
    ano_de_lancamento = models.IntegerField(null=True, blank=True)
    atores = models.ManyToManyField(Ator, related_name='filmes', blank=True)
    resumo = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.titulo