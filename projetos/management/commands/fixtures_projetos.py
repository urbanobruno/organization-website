from django.core.management import BaseCommand
from projetos.models import Tarefa, TipoTarefa, PrioridadeTarefa, Projeto
from home.models import Usuario


class Command(BaseCommand):

    def handle(self, *args, **options):

        Usuario.objects.create(
            nome='Bruno',
            sobrenome='Urbano',
            email='bruno.urbano.rocha@gmail.com'
        )

        list_prioridade = [
            'Alta',
            'Média',
            'Baixa'
        ]

        lista = []
        for p in list_prioridade:
            lista.append(
                PrioridadeTarefa(
                    descricao=p
                )
            )

        PrioridadeTarefa.objects.bulk_create(lista)

        list_tipos = [
            'Evento',
            'Lembrete',
            'Task'
        ]

        lista = []
        for t in list_tipos:
            lista.append(
                TipoTarefa(
                    descricao=t
                )
            )

        TipoTarefa.objects.bulk_create(lista)

        user = Usuario.objects.get(id=1)

        lista = []
        lista.append(Tarefa(
            titulo='Teste 1',
            descricao='Descricao 1',
            tipo_id=TipoTarefa.objects.get(id=1).id,
            prioridade_id=PrioridadeTarefa.objects.get(id=1).id,
            status=1,
            usuario_id=user.id
        ))

        lista.append(Tarefa(
            titulo='Teste 2',
            descricao='Descricao 2',
            tipo_id=TipoTarefa.objects.get(id=2).id,
            prioridade_id=PrioridadeTarefa.objects.get(id=2).id,
            status=2,
            usuario_id=user.id
        ))

        lista.append(Tarefa(
            titulo='Teste 3',
            descricao='Descricao 3',
            tipo_id=TipoTarefa.objects.get(id=3).id,
            prioridade_id=PrioridadeTarefa.objects.get(id=3).id,
            status=3,
            usuario_id=user.id,
        ))

        Tarefa.objects.bulk_create(lista)

        Projeto.objects.create(
            nome='Projeto 1',
            usuario_id=user.id,
        )

        for t in Tarefa.objects.all():
            Projeto.objects.get(id=1).tarefas.add(t.id)
