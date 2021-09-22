from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


# TIPO E PRIORIDADE COMO ETIQUETAS QUE PODE ADICIONAR A UMA TAREFA
# CADA TIPO E PRIORIDADE TEM UMA COR RANDOMIZADA QUE DEPOIS PODE SER ESCOLHIDA


class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    # to use universally
    # tipo = models.ManyToManyField('TipoTarefaProjeto', blank=True)
    # tipo = models.ManyToManyField('PrioridadeTarefaProjeto', blank=True)

    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'

    def __str__(self):
        return f'{self.nome}'


class TipoTarefaProjeto(models.Model):
    # Exemplo: pode ser um evento, uma tarefa, um lembrete, etc
    # Ja deixar criado
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=55)

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'

    def __str__(self):
        return self.descricao


# todo check foreign key -> many to one
class PrioridadeTarefaProjeto(models.Model):
    # Exemplo: alta, média, baixa
    # Ja deixar criado
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=55)

    class Meta:
        verbose_name = 'Prioridade'
        verbose_name_plural = 'Prioridades'

    def __str__(self):
        return self.descricao


class ListaTarefas(models.Model):
    nome = models.CharField(max_length=55, verbose_name='Nome da Lista')
    numero = models.IntegerField(default=1, editable=False)
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Lista de Tarefas'
        verbose_name_plural = 'Listas de Tarefas'
        ordering = ['numero']

    def __str__(self):
        return self.nome


class Tarefa(models.Model):
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    lista = models.ForeignKey(ListaTarefas, on_delete=models.CASCADE, blank=True, null=True)
    titulo = models.CharField(max_length=55, verbose_name='Título')
    descricao = models.TextField(max_length=255, blank=True, null=True, verbose_name='Descricão')
    tipo = models.ForeignKey(TipoTarefaProjeto, blank=True, null=True, on_delete=models.SET_NULL)
    prioridade = models.ForeignKey(PrioridadeTarefaProjeto, blank=True, null=True, on_delete=models.SET_NULL)
    data = models.DateField(blank=True, null=True, verbose_name='Data Final')
    ordem = models.IntegerField(default=1, editable=False)

    class Meta:
        verbose_name = 'Tarefa'
        verbose_name_plural = 'Tarefas'
        ordering = ['ordem']

    def __str__(self):
        return f'{self.titulo}'
