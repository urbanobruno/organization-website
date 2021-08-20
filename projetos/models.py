from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

# TODO ADICIONAR FEATURE PARA PODER ESCOLHER A COR DO BLOCK
# CASO NÃO ESCOLHIDO, RANDOMIZAR


class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'

    def __str__(self):
        return f'{self.nome}'


class TipoTarefa(models.Model):
    # Exemplo: pode ser um evento, uma tarefa, um lembrete, etc
    # Ja deixar criado
    descricao = models.CharField(max_length=50)
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'

    def __str__(self):
        return self.descricao


# todo chech foreign key -> many to one
class PrioridadeTarefa(models.Model):
    # Exemplo: alta, média, baixa
    # Ja deixar criado
    descricao = models.CharField(max_length=50)
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Prioridade'
        verbose_name_plural = 'Prioridades'

    def __str__(self):
        return self.descricao


class ListaTarefas(models.Model):
    nome = models.CharField(max_length=55, verbose_name='Nome da Lista')
    numero = models.IntegerField(default=1)
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)


class Tarefa(models.Model):
    titulo = models.CharField(max_length=100, blank=True, null=True, verbose_name='Título')
    descricao = models.TextField(max_length=255, blank=True, null=True, verbose_name='Descricão')
    tipo = models.ForeignKey(TipoTarefa, blank=True, null=True, on_delete=models.DO_NOTHING)
    prioridade = models.ForeignKey(PrioridadeTarefa, blank=True, null=True, on_delete=models.DO_NOTHING)
    data = models.DateField(blank=True, null=True, verbose_name='Data Final')
    lista = models.ForeignKey(ListaTarefas, on_delete=models.CASCADE)
    ordem = models.IntegerField(default=1)

    class Meta:
        verbose_name = 'Tarefa'
        verbose_name_plural = 'Tarefas'
        ordering = ['ordem']

    def clean(self):
        if not self.titulo and not self.descricao:
            raise ValidationError(
                {
                    'titulo': 'Informe ao menos um título ou uma descrição',
                    'descricao': 'Informe ao menos um título ou uma descrição',
                }
            )

    def __str__(self):
        return f'{self.titulo}' or f'{self.descricao}'

