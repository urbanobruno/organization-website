from django.contrib.auth.models import User
from django.core.management import BaseCommand
from projects.models import Task, PriorityTask, Project, TaskList
from random import randint


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Todo - change super user
        if not User.objects.all().exists():
            u = User.objects.create_superuser(
                username='admin',
                password='admin',
                email='bruno.urbano.rocha@gmail.com',
            )
        else:
            u = User.objects.get(username='admin')

        Project.objects.all().delete()
        TaskList.objects.all().delete()
        PriorityTask.objects.all().delete()
        Task.objects.all().delete()

        proj = Project.objects.create(
            name='Projeto 1',
            user_id=u.id,
        )

        list_tarefa_todo = TaskList.objects.create(
            name='list Todo',
            project_id=proj.id,
            order=1,
        )

        list_tarefa_doing = TaskList.objects.create(
            name='list Doing',
            project_id=proj.id,
            order=2,
        )

        list_tarefa_done = TaskList.objects.create(
            name='list Done',
            project_id=proj.id,
            order=3,
        )

        list_priority = [
            'Alta',
            'Média',
            'Baixa'
        ]

        list = []
        for p in list_priority:
            list.append(
                PriorityTask(
                    name=p,
                    project_id=proj.id,
                )
            )

        PriorityTask.objects.bulk_create(list)

        list_task = []

        # todo check range
        for x in range(1, 6):
            list_task.append(Task(
                project_id=proj.id,
                title=f'Todo {x}',
                description=f'Descricao TD {x}',
                priority_id=randint(1, 3),
                list_id=list_tarefa_todo.id,
                order=x
            ))

        for x in range(6, 11):
            list_task.append(Task(
                project_id=proj.id,
                title=f'Doing {x}',
                description=f'Descricao Dg {x}',
                priority_id=randint(1, 3),
                list_id=list_tarefa_doing.id,
                order=x
            ))

        for x in range(11, 16):
            list_task.append(Task(
                project_id=proj.id,
                title=f'Done {x}',
                description=f'Descricao Dn {x}',
                priority_id=randint(1, 3),
                list_id=list_tarefa_done.id,
                order=x
            ))

        Task.objects.bulk_create(list_task)
