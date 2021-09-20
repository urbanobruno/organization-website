from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.contrib import messages
from projetos.forms import CreateTaskForm
from projetos.models import Projeto, PrioridadeTarefaProjeto, Tarefa, TipoTarefaProjeto, ListaTarefas


def create_modal(
        request,
        form,
        url,
        title,
        refresh,
        obj_instance=None,
        form_initial=None,
        func_fix_form=None,
        success_msg=None,
):
    options_form = {'instance': obj_instance}
    if form_initial:
        options_form['initial'] = form_initial

    if request.method == 'POST':
        f = form(request.POST, **options_form)

        if func_fix_form:
            func_fix_form(form=f)

        if f.is_valid():
            s = f.save()

            if success_msg:
                messages.success(request, success_msg)

            response = HttpResponse()

            # todo define ids - make id content of whole page - content
            # response['X-IC-Script'] = f'Intercooler.refresh($("#{refresh}"));'

            return response

    # todo check if error think has to be post again
    f = form(**options_form)

    context = {
        'form': f,
        'url': url,
        'title': title
    }

    response = render(request, 'parciais/create_forms.html', context=context)

    # todo check toggle
    response['X-IC-Script'] = '$("#modal_base").modal("show");'

    return response


def base_projetos(request):
    projeto = Projeto.objects.get(id=1)

    # form = CreateTaskForm(initial={
    #     'projeto': projeto
    # })

    context = {
        'item': projeto,
        # 'form_create_task': form
    }

    return render(request, 'projetos/base.html', context=context)


# @login_required todo
def drag_list(request):
    list_id = int(request.GET.get('list_id'))
    target_list = request.GET.get('target')
    index_after = int(request.GET.get('index_after'))

    print(list_id)
    print(target_list)
    print(index_after)

    lista = ListaTarefas.objects.get(id=list_id)

    # try:
    #     new_numero = Tarefa.objects.filter(
    #         projeto_id=project_id,
    #         status__gte=dictionary[target_list],
    #     )[index_after].ordem
    # except IndexError:
    #     new_numero = Tarefa.objects.filter(
    #         projeto_id=project_id,
    #         status__lte=dictionary[target_list],
    #     ).last().ordem
    #
    # Tarefa.objects.filter(
    #     id=tarefa_id
    # ).update(
    #     status=dictionary[target_list],
    #     ordem=new_order
    # )
    #
    # Tarefa.objects.filter(
    #     projeto_id=project_id,
    #     ordem__gte=new_order,
    # ).exclude(id=tarefa_id).update(ordem=F('ordem') + 1)

    return HttpResponse()


# @login_required todo


# @login_required todo
def drag_task(request, project_id):
    tarefa_id = int(request.GET.get('tarefa_id'))
    target_list = int(request.GET.get('target'))
    index_after = int(request.GET.get('index_after'))

    # Todo: check with one task

    try:
        new_order = Tarefa.objects.filter(
            projeto_id=project_id,
            lista__numero__gte=target_list,
        )[index_after].ordem
    except IndexError:
        new_order = Tarefa.objects.filter(
            projeto_id=project_id,
            lista__numero__lte=target_list,
        ).last().ordem

    Tarefa.objects.filter(
        id=tarefa_id
    ).update(
        lista_id=ListaTarefas.objects.get(projeto_id=project_id, numero=target_list),
        ordem=new_order
    )

    Tarefa.objects.filter(
        projeto_id=project_id,
        lista__isnull=False,
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
def create_task(request, lista_id):
    lista = ListaTarefas.objects.get(id=lista_id)

    def fix_form(form):
        form.instance.lista_id = lista.id

    return create_modal(
        request,
        CreateTaskForm,
        f'/create_task/{lista_id}',
        'Create New Task',
        'projetos',
        form_initial={'projeto': lista.projeto},
        func_fix_form=fix_form,
        success_msg='Task create successfully',
    )


# def create_task(request, lista_id):
#     lista = ListaTarefas.objects.get(id=lista_id)
#     projeto = lista.projeto
#
#     if request.method == 'POST':
#         form = CreateTaskForm(request.POST, initial={
#             'projeto': projeto
#         })
#
#         form.instance.lista_id is lista_id
#         # form.instance.ordem = lista.tarefa_set.first().ordem
#
#         # Tarefa.objects.filter(
#         #     lista__numero__gte=lista.numero,
#         # ).update(ordem=F('ordem') + 1)
#
#         if form.is_valid():
#             form.save()
#
#             messages.success(request, 'Task create successfully')
#
#             return HttpResponseRedirect(reverse('projetos'))
#
#     form = CreateTaskForm(initial={
#         'projeto': projeto
#     })
#
#     # todo check url
#     # print(request.GET.get('url'))
#     # print(type(request.build_absolute_uri()))
#     # print(type(request.get_full_path()))
#
#     context = {
#         'form': form,
#         'url': f'/create_task/{lista_id}',
#         'title': 'Create New Task'
#     }
#
#     response = render(request, 'parciais/create_forms.html', context=context)
#
#     response['X-IC-Script'] = '$("#modal_base").modal("show");'
#
#     return response


# @login_required todo
# @require_POST
def create_type_task(request, project_id):
    desc = request.POST.get('type', None)

    print(desc)
    print(request.method)

    if request.method == "POST":
        if desc:
            TipoTarefaProjeto.objects.create(
                descricao=desc,
                projeto_id=project_id
            )

    # todo check url
    return HttpResponseRedirect(reverse('projetos'))


# @login_required todo
# @require_POST
def create_priority_task(request, project_id):
    desc = request.POST.get('priority', None)

    if request.method == "POST":
        if desc:
            PrioridadeTarefaProjeto.objects.create(
                descricao=desc,
                projeto_id=project_id
            )

    # todo check url
    return HttpResponseRedirect(reverse('projetos'))

def edit_type(request, type_id):
    pass


def delete_type(request, type_id):
    return HttpResponse()


def edit_priority(request, priority_id):
    pass


def delete_priority(request, priority_id):
    return HttpResponse()

def edit_list(request, lista_id):
    pass


def delete_list(request, lista_id):
    return HttpResponse()
