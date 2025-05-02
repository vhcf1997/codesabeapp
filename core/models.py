from django.db import models

class Nota(models.Model):
    tipo = models.CharField(max_length=10, verbose_name='tipo')
    nome = models.CharField(max_length=100, verbose_name='nome')
    linguagem = models.CharField(max_length=10, verbose_name='linguagem')
    descricao = models.TextField(verbose_name='descricao')
    exemplo = models.TextField(verbose_name='exemplo')
    palavraChave = models.TextField(verbose_name='palavra chave')
    dataCriacao = models.DateTimeField(verbose_name='data de criacao')
    dataEdicao = models.DateTimeField(verbose_name='data de edicao')

    def __str__(self):
        return self.nome
