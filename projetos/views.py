from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.decorators.http import require_POST

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


# TODO check csrf_exempt
def drag_task(request, project_id):
    p = Projeto.objects.get(id=project_id)

    target_list = request.GET.get('target')
    previous_list = request.GET.get('previous')
    index_before = request.GET.get('index_before')
    index_after = request.GET.get('index_after')

    print(target_list)
    print(previous_list)
    print(index_before)
    print(index_after)



    return HttpResponse()

