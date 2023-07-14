from django.db import models

# Create your models here.
from django.db import models


class Personagens(models.Model):
    objects = None
    personagem = models.CharField(max_length=100)
    jogo = models.CharField(max_length=100)
    ano = models.IntegerField()
