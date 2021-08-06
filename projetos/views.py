from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from projetos.models import Usuario, Projeto, PrioridadeTarefa, Tarefa, TipoTarefa
# Create your views here.


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
