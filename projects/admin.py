from django.contrib import admin
from .models import Project, PriorityTask, Task, TaskList


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user')
    list_display_links = ('id',)
    list_editable = ('name', )


class TaskListAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'order', 'project')
    list_display_links = ('id', )
    list_editable = ('name', )


class PriorityTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'project')
    list_display_links = ('id', )
    list_editable = ('name',)


class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'description',
        'priority',
        'date',
        'order',
        'list',
        'project',
    )
    list_display_links = (
        'id',
    )
    list_editable = (
        'title',
        'description',
        'priority',
        'date',
    )
    
    
admin.site.register(Project, ProjectAdmin)
admin.site.register(TaskList, TaskListAdmin)
admin.site.register(PriorityTask, PriorityTaskAdmin)
admin.site.register(Task, TaskAdmin)
