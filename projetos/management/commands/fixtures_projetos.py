from django.contrib.auth.models import User
from django.core.management import BaseCommand
from projetos.models import Tarefa, TipoTarefa, PrioridadeTarefa, Projeto


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

        lista = []
        lista.append(Tarefa(
            id=1,
            titulo='Teste 1',
            descricao='Descricao 1',
            tipo_id=TipoTarefa.objects.get(id=1).id,
            prioridade_id=PrioridadeTarefa.objects.get(id=1).id,
            status=1,
            projeto_id=proj.id,
        ))

        lista.append(Tarefa(
            id=2,
            titulo='Teste 2',
            descricao='Descricao 2',
            tipo_id=TipoTarefa.objects.get(id=2).id,
            prioridade_id=PrioridadeTarefa.objects.get(id=2).id,
            status=2,
            projeto_id=proj.id,
        ))

        lista.append(Tarefa(
            id=3,
            titulo='Teste 3',
            descricao='Descricao 3',
            tipo_id=TipoTarefa.objects.get(id=3).id,
            prioridade_id=PrioridadeTarefa.objects.get(id=3).id,
            status=3,
            projeto_id=proj.id,
        ))

        Tarefa.objects.bulk_create(lista)
