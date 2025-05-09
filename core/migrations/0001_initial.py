# Generated by Django 5.2 on 2025-05-02 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=10, verbose_name='tipo')),
                ('nome', models.CharField(max_length=100, verbose_name='nome')),
                ('linguagem', models.CharField(max_length=10, verbose_name='linguagem')),
                ('descricao', models.TextField(verbose_name='descricao')),
                ('exemplo', models.TextField(verbose_name='exemplo')),
                ('palavraChave', models.TextField(verbose_name='palavra chave')),
                ('dataCriacao', models.DateTimeField(verbose_name='data de criacao')),
                ('dataEdicao', models.DateTimeField(verbose_name='data de edicao')),
            ],
        ),
    ]
