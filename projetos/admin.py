from django.contrib import admin
from .models import TipoTarefaProjeto, PrioridadeTarefaProjeto, Tarefa, Projeto


class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'usuario')
    list_display_links = ('id',)
    list_editable = ('nome', )


class TipoTarefaProjetoAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao')
    list_display_links = ('id', )
    list_editable = ('descricao',)


class PrioridadeTarefaProjetoAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao')
    list_display_links = ('id', )
    list_editable = ('descricao',)


class TarefaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'titulo',
        'descricao',
        'tipo',
        'prioridade',
        'data',
        'lista',
        'ordem',
    )
    list_display_links = (
        'id',
    )
    list_editable = (
        'titulo',
        'descricao',
        'tipo',
        'prioridade',
        'data',
    )


admin.site.register(TipoTarefaProjeto, TipoTarefaProjetoAdmin)
admin.site.register(PrioridadeTarefaProjeto, PrioridadeTarefaProjetoAdmin)
admin.site.register(Tarefa, TarefaAdmin)
admin.site.register(Projeto, ProjetoAdmin)
