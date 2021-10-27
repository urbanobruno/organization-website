from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


# todo ver como fica os templates com a descrição no 255
from django.utils.timezone import localtime


class Project(models.Model):
    name = models.CharField(max_length=75)
    description = models.TextField(max_length=300, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(editable=False, null=True, blank=True)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ['updated_at', 'created_at']

    def __str__(self):
        return self.name

    # todo check
    def save(self, *args, **kwargs):
        self.updated_at = localtime()
        super().save(*args, **kwargs)


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
    name = models.CharField(max_length=55)
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
    title = models.CharField(max_length=55, verbose_name='Title')
    description = models.TextField(max_length=255, blank=True, null=True, verbose_name='Description')
    priority = models.ForeignKey(PriorityTask, blank=True, null=True, on_delete=models.SET_NULL)
    date = models.DateField(blank=True, null=True, verbose_name='Date')
    start_time = models.TimeField(null=True, blank=True, verbose_name='Starting Time')
    final_time = models.TimeField(null=True, blank=True, verbose_name='Final Time')
    order = models.IntegerField(default=1, editable=False)

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Task'
        ordering = ['order']

    def __str__(self):
        return self.title
