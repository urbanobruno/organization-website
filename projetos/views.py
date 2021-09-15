from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib import messages
from projetos.forms import CreateTaskForm
from projetos.models import Projeto, PrioridadeTarefaProjeto, Tarefa, TipoTarefaProjeto, ListaTarefas


def create_form_html():
    pass



# @login_required todo
def base_projetos(request):
    projeto = Projeto.objects.get(id=1)

    form = CreateTaskForm(initial={
        'projeto': projeto
    })

    context = {
        'item': projeto,
        'form_create_task': form
    }

    return render(request, 'projetos/base.html', context=context)


def create_modal(request):
    print('Testando')
    params = {
        'url': request.GET.get('url'),
        'form': request.GET.get('form'),
        'target': request.GET.get('target_id'),
        'title': request.GET.get('title'),
        'edit': request.GET.get('edit', False),
    }
    response = render(request,
                      'parciais/create_forms.html',
                      context=params)

    response['X-IC-Script'] = f"$(#{params['target_id']}).modal('show')"

    return response

    # <script>
    #     $('*[id*=Modal]').each(function () {
    #         $(this.id).on('show.bs.modal', function (event) {
    #             var button = $(event.relatedTarget) // Button that triggered the modal
    #             {#var recipient = button.data('whatever') // Extract info from data-* attributes#}
    #             // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
    #             // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
    #
    #             console.log("TESTANDO")
    #             console.log("TESTANDO")
    #
    #             var modal = $(this)
    #             modal.find('.modal-title').text('New message to ' + recipient)
    #             modal.find('.modal-body input').val(recipient)
    #         })
    #
    #         console.log(this);
    #         console.log(this.id);
    #         console.log($(this))
    #     });
    #
    # </script>


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
    projeto = lista.projeto

    if request.method == 'POST':
        form = CreateTaskForm(request.POST, initial={
            'projeto': projeto
        })

        form.instance.lista_id = lista_id
        form.instance.ordem = lista.tarefa_set.first().ordem

        Tarefa.objects.filter(
            lista__numero__gte=lista.numero,
        ).update(ordem=F('ordem') + 1)

        if form.is_valid():
            form.save()

            messages.success(request, 'Task create successfully')

            return HttpResponseRedirect(reverse('projetos'))

    # form = CreateTaskForm()
    #
    # return render(request, 'parciais/form_create_task.html',
    #               {
    #                   'form': form,
    #                   'lista_id': lista_id
    #               })

    # if request.method == 'POST':
    #     form = CreateTask(request.POST, initial={
    #         'projeto': p,
    #         'status': status
    #     })
    #     if form.is_valid():
    #         form.save()

    # return HttpResponseRedirect(reverse('projetos'))


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
