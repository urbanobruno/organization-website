from django.contrib import admin
from .models import TipoTarefa, PrioridadeTarefa, Tarefa


class TipoTarefaAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao')
    list_editable = ('descricao',)


class PrioridadeTarefaAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao')
    list_editable = ('descricao',)


class TarefaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'titulo',
        'descricao',
        'tipo',
        'prioridade',
        'data_criacao',
        'data_final'
    )
    list_editable = (
        'titulo',
        'descricao',
        'tipo',
        'prioridade',
        'data_final'
    )


admin.site.register(TipoTarefa, TipoTarefaAdmin)
admin.site.register(PrioridadeTarefa, PrioridadeTarefaAdmin)
admin.site.register(Tarefa, TarefaAdmin)
