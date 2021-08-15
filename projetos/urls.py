from django.urls import path
from . import views

urlpatterns = [
    path('',
        views.base_projetos,
        name='projetos'),
    path('drag_task/<int:project_id>',
         views.drag_task,
         name='drag_task'),
]
