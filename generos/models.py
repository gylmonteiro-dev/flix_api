from django.db import models

# Create your models here.
class GeneroModel(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome
    

class AtorModel(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11)
    idade  = models.FloatField()

    def __str__(self):
        return self.nome