from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.decorators.http import require_POST

# from projetos.forms import CreateTask
from projetos.models import Projeto, PrioridadeTarefa, Tarefa, TipoTarefa


# @login_required todo
def base_projetos(request):
    projeto = Projeto.objects.get(id=1)

    # form_task = CreateTask

    context = {
        'item': projeto,
        # 'form_task': form_task,
    }

    return render(request, 'projetos/base.html', context=context)


# @login_required todo
def drag_task(request, project_id):
    tarefa_id = int(request.GET.get('tarefa'))
    target_list = request.GET.get('target')
    index_after = int(request.GET.get('index_after'))

    dictionary = {
        'todo': 1,
        'doing': 2,
        'done': 3,
    }


    try:
        new_order = Tarefa.objects.filter(
            projeto_id=project_id,
            status__gte=dictionary[target_list],
        )[index_after].ordem
    except IndexError:
        new_order = Tarefa.objects.filter(
            projeto_id=project_id,
            status__lte=dictionary[target_list],
        ).last().ordem

    Tarefa.objects.filter(
        id=tarefa_id
    ).update(
        status=dictionary[target_list],
        ordem=new_order
    )

    Tarefa.objects.filter(
        projeto_id=project_id,
        ordem__gte=new_order,
    ).exclude(id=tarefa_id).update(ordem=F('ordem') + 1)

    return HttpResponse()


# def contact_view(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = ContactForm()
#
#     context = {'form': form}
#     return render(request, 'contacts/contact_page.html', context)

# @login_required todo
def create_task(request, projeto_id, status):
    p = Projeto.objects.get(pk=projeto_id)

    print(request.method)
    print('TESTANDO')
    print('TESTANDO')

    # if request.method == 'POST':
    #     form = CreateTask(request.POST, initial={
    #         'projeto': p,
    #         'status': status
    #     })
    #     if form.is_valid():
    #         form.save()

    return HttpResponseRedirect(reverse('projetos'))


# @login_required todo
# @require_POST
def create_type_task(request, project_id):
    desc = request.POST.get('type', None)

    print(desc)
    print(request.method)

    if request.method == "POST":
        if desc:
            TipoTarefa.objects.create(
                descricao=desc,
                projeto_id=project_id
            )

    return HttpResponseRedirect(reverse('projetos'))


# @login_required todo
# @require_POST
def create_priority_task(request, project_id):
    desc = request.POST.get('priority', None)

    if request.method == "POST":
        if desc:
            PrioridadeTarefa.objects.create(
                descricao=desc,
                projeto_id=project_id
            )

    return HttpResponseRedirect(reverse('projetos'))
