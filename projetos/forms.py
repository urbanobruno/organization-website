from django import forms
from django.core.exceptions import ValidationError
from django.forms import HiddenInput

from projetos.models import Tarefa, TipoTarefaProjeto, PrioridadeTarefaProjeto, ListaTarefas


class CreateTaskForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        project_id = kwargs['initial']['projeto'].id
        self.fields['tipo'].queryset = TipoTarefaProjeto.objects.filter(
            projeto_id=project_id
        )
        self.fields['prioridade'].queryset = PrioridadeTarefaProjeto.objects.filter(
            projeto_id=project_id
        )

    class Meta:
        model = Tarefa
        fields = [
            'titulo',
            'descricao',
            'tipo',
            'prioridade',
            'data',
            'projeto'
        ]
        widgets = {
            'projeto': HiddenInput
        }

