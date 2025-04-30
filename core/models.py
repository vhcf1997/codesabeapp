from django.db import models


class Item(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    exemplo = models.TextField(blank=True, null=True)
    linguagem = models.CharField(max_length=50, blank=True, null=True)
    tipo = models.CharField(max_length=50)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

    @property
    def tipo_badge(self):
        # Retorna a classe Bootstrap baseada no tipo
        return {
            'biblioteca': 'primary',
            'função': 'success',
            'classe': 'info',
        }.get(self.tipo, 'secondary')