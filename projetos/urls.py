from django.urls import path
from . import views


urlpatterns = [
    path('',
         views.base_projetos,
         name='projetos'),
    path('drag_list',
         views.drag_list,
         name='drag_list'),
    path('drag_task/<int:project_id>',
         views.drag_task,
         name='drag_task'),
    path('edit_list/<int:lista_id>',
         views.edit_list,
         name='edit_list'),
    path('delete_list/<int:lista_id>',
         views.delete_list,
         name='delete_list'),
    path('create_task/<int:lista_id>',
         views.create_task,
         name='create_task'),
    path('create_type_task/<int:project_id>',
         views.create_type_task,
         name='create_type_task'),
    path('create_priority_task/<int:project_id>',
         views.create_priority_task,
         name='create_priority_task'),
    path('edit_type/<int:type_id>',
         views.edit_type,
         name='edit_type'),
    path('delete_type/<int:type_id>',
         views.delete_type,
         name='delete_type'),
    path('edit_priority/<int:priority_id>',
         views.edit_priority,
         name='edit_priority'),
    path('delete_priority/<int:priority_id>',
         views.delete_priority,
         name='delete_priority'),
]
