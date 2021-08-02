from django.shortcuts import render

# Create your views here.

def base_calendario(request):
    return render(request, 'barra_superior.html')