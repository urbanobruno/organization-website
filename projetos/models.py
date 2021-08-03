from django.core.exceptions import ValidationError
from django.db import models
from datetime import datetime

from django.utils import timezone

from home.models import Usuario


# TODO ADICIONAR FEATURE PARA PODER ESCOLHER A COR DO BLOCK
# CASO NÃO ESCOLHIDO, RANDOMIZAR


class TipoTarefa(models.Model):
    # Exemplo: pode ser um evento, uma tarefa, um lembrete, etc
    # Ja deixar criado
    descricao = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'


class PrioridadeTarefa(models.Model):
    # Exemplo: alta, média, baixa
    # Ja deixar criado
    descricao = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Prioridade'
        verbose_name_plural = 'Prioridades'


class Tarefa(models.Model):
    STATUS = (
        (1, 'To Do'),
        (2, 'Doing'),
        (3, 'Done'),
    )

    titulo = models.CharField(max_length=100, blank=True, null=True)
    descricao = models.TextField(max_length=255, blank=True, null=True)
    tipo = models.ForeignKey(TipoTarefa, blank=True, null=True, on_delete=models.DO_NOTHING)
    prioridade = models.ForeignKey(PrioridadeTarefa, blank=True, null=True, on_delete=models.DO_NOTHING)
    data_criacao = models.DateTimeField(default=timezone.now, editable=False)
    data_final = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(choices=STATUS, default=1)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    verbose_name = 'Tarefa'
    verbose_name_plural = 'Tarefas'

    def clean(self):
        if not self.titulo and not self.descricao:
            raise ValidationError(
                {
                    'titulo': 'Informe ao menos um título ou uma descrição',
                    'descricao': 'Informe ao menos um título ou uma descrição',
                }
            )

    def __str__(self):
        return f'{self.titulo}'

    def status_display(self):
        return self.STATUS[self.status]

    # TODO: check -- filter user
    # check if user has to be in projetos and in tarefa


# TODO: poder criar mais de um projeto e poder atribuir tarefas a ele
class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    tarefas = models.ManyToManyField(Tarefa)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def tarefas_to_do(self):
        return self.tarefas.filter(
            status=1
        )

    def tarefas_doing(self):
        return self.tarefas.filter(
            status=2
        )

    def tarefas_done(self):
        return self.tarefas.filter(
            status=3
        )
