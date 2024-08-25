from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    index = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=45)

    def __str__(self):
        return self.nome
class Produto(models.Model):
    index = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=60)
    descricao = models.CharField(max_length=200)
    preco = models.IntegerField()
    ativo = models.BooleanField(default=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    usuario =  models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
