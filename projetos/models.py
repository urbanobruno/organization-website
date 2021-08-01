from django.db import models
from datetime import datetime


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
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(max_length=255)
    tipo = models.ForeignKey(TipoTarefa, blank=True, null=True, on_delete=models.DO_NOTHING)
    prioridade = models.ForeignKey(PrioridadeTarefa, blank=True, null=True, on_delete=models.DO_NOTHING)
    data_criacao = models.DateTimeField(default=datetime.now(), editable=False)
    data_final = models.DateTimeField()

    verbose_name = 'Tarefa'
    verbose_name_plural = 'Tarefas'

    def __str__(self):
        return f'{self.titulo}'
