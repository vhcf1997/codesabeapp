from django.db import models

class Linguagem(models.Model):
    nome = models.CharField(max_length=20, verbose_name='nome')

    def __str__(self):
        return self.nome

class Nota(models.Model):
    tipo = models.CharField(max_length=20, verbose_name='tipo')
    nome = models.CharField(max_length=100, verbose_name='nome')
    linguagem = models.ForeignKey(Linguagem, on_delete=models.CASCADE)
    descricao = models.TextField(max_length=200, verbose_name='descricao')
    exemplo = models.TextField(max_length=200, verbose_name='exemplo')
    palavraChave = models.TextField(verbose_name='palavra chave')
    dataCriacao = models.DateTimeField(auto_now_add=True)
    dataEdicao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome