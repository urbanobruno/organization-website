from projetos.forms import *
from django import template

register = template.Library()


@register.simple_tag
def call_form_initial(form_name, projeto, status):
    form = form_name
    form.__init__(initial={
        'projeto': projeto,
        'status': status,
    })
    return form
