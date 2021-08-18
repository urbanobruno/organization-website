from django.urls import path
from . import views

urlpatterns = [
    path('',
         views.base_projetos,
         name='projetos'),
    path('drag_task/<int:project_id>',
         views.drag_task,
         name='drag_task'),
    path('create_task/<int:projeto_id>/<int:status>',
         views.create_task,
         name='create_task'),
    path('create_type_task/<int:projeto_id>',
         views.create_type_task,
         name='create_type_task'),
    path('create_priority_task/<int:projeto_id>',
         views.create_priority_task,
         name='create_priority_task'),
]
