from django.shortcuts import render

# Create your views here.

def base_projetos(request):
    return render(request, 'barra_superior.html')
