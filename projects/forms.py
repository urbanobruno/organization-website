from django import forms
from django.core.exceptions import ValidationError
from django.forms import HiddenInput

from projects.models import Task, TaskList, Project, PriorityTask


class CreateTaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        project_id = kwargs['initial']['project'].id
        self.fields['priority'].queryset = PriorityTask.objects.filter(
            project_id=project_id
        )

    class Meta:
        model = Task
        fields = [
            'title',
            'description',
            'priority',
            'date',
            'project'
        ]
        widgets = {
            'project': HiddenInput
        }


class EditPriorityForm(forms.ModelForm):
    class Meta:
        model = PriorityTask
        fields = [
            'name'
        ]


class EditListForm(forms.ModelForm):
    class Meta:
        model = TaskList
        fields = [
            'name'
        ]
