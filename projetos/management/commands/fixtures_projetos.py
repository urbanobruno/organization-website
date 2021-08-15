from django.contrib.auth.models import User
from django.core.management import BaseCommand
from projetos.models import Tarefa, TipoTarefa, PrioridadeTarefa, Projeto
from random import randint

class Command(BaseCommand):

    def handle(self, *args, **options):

        User.objects.all().delete()
        Projeto.objects.all().delete()
        TipoTarefa.objects.all().delete()
        PrioridadeTarefa.objects.all().delete()
        Tarefa.objects.all().delete()

        # TODO: rodar novamente

        u = User.objects.create(
            id=1,
            username='brunourbano',
            first_name='Bruno',
            last_name='Urbano',
            email='teste@gmail.com'
        )

        proj = Projeto.objects.create(
            id=1,
            nome='Projeto 1',
            usuario_id=u.id,
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
                id=x,
                titulo=f'Todo {x}',
                descricao=f'Descricao TD {x}',
                tipo_id=randint(1, 3),
                prioridade_id=randint(1, 3),
                status=1,
                projeto_id=proj.id,
                ordem=x
            ))

        for x in range(6, 10):
            lista_criar.append(Tarefa(
                id=x,
                titulo=f'Doing {x}',
                descricao=f'Descricao Dg {x}',
                tipo_id=randint(1, 3),
                prioridade_id=randint(1, 3),
                status=2,
                projeto_id=proj.id,
                ordem=x
            ))

        for x in range(11, 15):
            lista_criar.append(Tarefa(
                id=x,
                titulo=f'Done {x}',
                descricao=f'Descricao Dn {x}',
                tipo_id=randint(1, 3),
                prioridade_id=randint(1, 3),
                status=3,
                projeto_id=proj.id,
                ordem=x
            ))

        Tarefa.objects.bulk_create(lista_criar)
