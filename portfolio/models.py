from django.db import models

# Create your models here.

class Blog(models.Model):

    autor = models.CharField(max_length=40)
    data = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=40)
    descricao = models.TextField()

    def __str__(self):
        return self.titulo[:50]

class PontuacaoQuizz(models.Model):
    nome = models.CharField(max_length = 40)
    pontuacao = models.IntegerField(default = 0)

    def __str__(self):
        return self.nome