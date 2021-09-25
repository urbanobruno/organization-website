from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

# todo ver como fica os templates com a descrição no 255
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(default=timezone.now, editable=False)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.name


# todo deixar criado ja high(red), medium(yellow), low(green) - check
class PriorityTask(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=55)

    class Meta:
        verbose_name = 'Priority'
        verbose_name_plural = 'Priorities'

    def __str__(self):
        return self.name


class TaskList(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=55, verbose_name='Nome da Lista')
    order = models.IntegerField(default=1, editable=False)

    class Meta:
        verbose_name = 'Task List'
        verbose_name_plural = 'Task Lists'
        ordering = ['order']

    def __str__(self):
        return self.name


class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    list = models.ForeignKey(TaskList, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=55, verbose_name='Título')
    description = models.TextField(max_length=255, blank=True, null=True, verbose_name='Descricão')
    priority = models.ForeignKey(PriorityTask, blank=True, null=True, on_delete=models.SET_NULL)
    date = models.DateField(blank=True, null=True, verbose_name='Data Final')
    order = models.IntegerField(default=1, editable=False)

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Task'
        ordering = ['order']

    def __str__(self):
        return self.title
