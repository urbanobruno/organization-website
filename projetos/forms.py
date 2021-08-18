from django import forms
from django.forms import HiddenInput

from projetos.models import Tarefa, TipoTarefa, PrioridadeTarefa


class CreateTask(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if kwargs.get('initial', None):
            initial = kwargs['initial']
            project_id = initial['projeto'].id
            self.fields['tipo'].queryset = TipoTarefa.objects.filter(
                projeto_id=project_id
            )
            self.fields['prioridade'].queryset = PrioridadeTarefa.objects.filter(
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
            'status',
            'projeto',
        ]
        widgets = {
            'status': HiddenInput,
            'projeto': HiddenInput,
        }


