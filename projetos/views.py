from django.shortcuts import render
from projetos.models import Projeto, PrioridadeTarefa, Tarefa, TipoTarefa
# Create your views here.


def base_projetos(request):
    projeto = Projeto.objects.get(id=1)

    context = {
        'item': projeto
    }

    return render(request, 'projetos/base.html', context=context)
