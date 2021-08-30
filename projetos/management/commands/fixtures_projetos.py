from django.contrib.auth.models import User
from django.core.management import BaseCommand
from projetos.models import Tarefa, TipoTarefaProjeto, PrioridadeTarefaProjeto, Projeto, ListaTarefas
from random import randint


class Command(BaseCommand):

    def handle(self, *args, **options):

        if not User.objects.all().exists():
            u = User.objects.create_superuser(
                username='admin',
                password='admin',
                email='bruno.urbano.rocha@gmail.com',
            )
        else:
            u = User.objects.all().first()
        # User.objects.all().delete()
        Projeto.objects.all().delete()
        ListaTarefas.objects.all().delete()
        TipoTarefaProjeto.objects.all().delete()
        PrioridadeTarefaProjeto.objects.all().delete()
        Tarefa.objects.all().delete()

        proj = Projeto.objects.create(
            nome='Projeto 1',
            usuario_id=u.id,
        )

        lista_tarefa_todo = ListaTarefas.objects.create(
            nome='Lista Todo',
            projeto_id=proj.id,
            numero=1,
        )

        lista_tarefa_doing = ListaTarefas.objects.create(
            nome='Lista Doing',
            projeto_id=proj.id,
            numero=2,
        )

        lista_tarefa_done = ListaTarefas.objects.create(
            nome='Lista Done',
            projeto_id=proj.id,
            numero=3,
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
                PrioridadeTarefaProjeto(
                    descricao=p,
                    projeto_id=proj.id,
                )
            )
            x += 1

        PrioridadeTarefaProjeto.objects.bulk_create(lista)

        list_tipos = [
            'Evento',
            'Lembrete',
            'Task'
        ]

        lista = []
        x = 1
        for t in list_tipos:
            lista.append(
                TipoTarefaProjeto(
                    descricao=t,
                    projeto_id=proj.id,
                )
            )
            x += 1

        TipoTarefaProjeto.objects.bulk_create(lista)

        lista_criar = []

        for x in range(1, 5):
            lista_criar.append(Tarefa(
                projeto_id=proj.id,
                titulo=f'Todo {x}',
                descricao=f'Descricao TD {x}',
                tipo_id=randint(1, 3),
                prioridade_id=randint(1, 3),
                lista_id=lista_tarefa_todo.id,
                ordem=x
            ))

        for x in range(6, 10):
            lista_criar.append(Tarefa(
                projeto_id=proj.id,
                titulo=f'Doing {x}',
                descricao=f'Descricao Dg {x}',
                tipo_id=randint(1, 3),
                prioridade_id=randint(1, 3),
                lista_id=lista_tarefa_doing.id,
                ordem=x
            ))

        for x in range(11, 15):
            lista_criar.append(Tarefa(
                projeto_id=proj.id,
                titulo=f'Done {x}',
                descricao=f'Descricao Dn {x}',
                tipo_id=randint(1, 3),
                prioridade_id=randint(1, 3),
                lista_id=lista_tarefa_done.id,
                ordem=x
            ))

        Tarefa.objects.bulk_create(lista_criar)
