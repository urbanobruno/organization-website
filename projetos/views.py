from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from projetos.models import Projeto, PrioridadeTarefa, Tarefa, TipoTarefa


# @login_required
def base_projetos(request):
    projeto = Projeto.objects.get(id=1)

    context = {
        'item': projeto
    }

    return render(request, 'projetos/base.html', context=context)


@login_required
def adicionar_tipo(request, projeto_id, descricao):
    pass
    # TipoTarefa.objects.create(
    #     descricao=descricao,
    #     projeto_id=projeto_id,
    # )
