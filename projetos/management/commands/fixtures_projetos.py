from django.contrib.auth.models import User
from django.core.management import BaseCommand
from projetos.models import Tarefa, TipoTarefa, PrioridadeTarefa, Projeto, ListaTarefas
from random import randint


class Command(BaseCommand):

    def handle(self, *args, **options):

        # User.objects.all().delete()
        Projeto.objects.all().delete()
        ListaTarefas.objects.all().delete()
        TipoTarefa.objects.all().delete()
        PrioridadeTarefa.objects.all().delete()
        Tarefa.objects.all().delete()

        u = User.objects.get(
            username='admin',
        )

        print(u.id)

        proj = Projeto.objects.create(
            id=1,
            nome='Projeto 1',
            usuario_id=u.id,
        )

        lista_tarefa_todo = ListaTarefas.objects.create(
            nome='Lista Done',
            projeto_id=proj.id,
            numero=1,
        )

        lista_tarefa_doing = ListaTarefas.objects.create(
            nome='Lista Doing',
            projeto_id=proj.id,
            numero=1,
        )

        lista_tarefa_done = ListaTarefas.objects.create(
            nome='Lista Done',
            projeto_id=proj.id,
            numero=1,
        )

        list_prioridade = [
            'Alta',
            'Média',
            'Baixa'
        ]

        lista = []
        x = 1
        for p in list_prioridade:
            lista.append(
                PrioridadeTarefa(
                    id=x,
                    descricao=p,
                    projeto_id=proj.id,
                )
            )
            x += 1

        PrioridadeTarefa.objects.bulk_create(lista)

        list_tipos = [
            'Evento',
            'Lembrete',
            'Task'
        ]

        lista = []
        x = 1
        for t in list_tipos:
            lista.append(
                TipoTarefa(
                    id=x,
                    descricao=t,
                    projeto_id=proj.id,
                )
            )
            x += 1

        TipoTarefa.objects.bulk_create(lista)

        lista_criar = []

        for x in range(1, 5):
            lista_criar.append(Tarefa(
                titulo=f'Todo {x}',
                descricao=f'Descricao TD {x}',
                tipo_id=randint(1, 3),
                prioridade_id=randint(1, 3),
                lista_id=lista_tarefa_todo.id,
                ordem=x
            ))

        for x in range(6, 10):
            lista_criar.append(Tarefa(
                titulo=f'Doing {x}',
                descricao=f'Descricao Dg {x}',
                tipo_id=randint(1, 3),
                prioridade_id=randint(1, 3),
                lista_id=lista_tarefa_doing.id,
                ordem=x
            ))

        for x in range(11, 15):
            lista_criar.append(Tarefa(
                titulo=f'Done {x}',
                descricao=f'Descricao Dn {x}',
                tipo_id=randint(1, 3),
                prioridade_id=randint(1, 3),
                lista_id=lista_tarefa_done.id,
                ordem=x
            ))

        Tarefa.objects.bulk_create(lista_criar)
