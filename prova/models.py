from django.db import models

# Create your models here.
class Pessoa (models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.IntegerField()
    idade = models.IntegerField()
    sexo = models.CharField(max_length=1)

    def __str__(self):
        return self.nome
