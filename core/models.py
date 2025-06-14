from django.db import models
from django.contrib.auth.models import User

class Linguagem(models.Model):
    nome = models.CharField(max_length=20, verbose_name='nome')

    def __str__(self):
        return self.nome

class Nota(models.Model):
    tipo = models.CharField(max_length=20, verbose_name='tipo')
    nome = models.CharField(max_length=100, verbose_name='nome')
    linguagem = models.ForeignKey(Linguagem, on_delete=models.CASCADE)
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='notas',
        null=True,
        blank=True,
    )
    descricao = models.TextField(max_length=200, verbose_name='descricao')
    exemplo = models.TextField(max_length=200, verbose_name='exemplo')
    palavraChave = models.TextField(verbose_name='palavra chave')
    dataCriacao = models.DateTimeField(auto_now_add=True)
    dataEdicao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome


class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:

        # Ensure a profile exists for existing users
        Profile.objects.get_or_create(user=instance)
        instance.profile.save()


