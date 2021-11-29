from django.shortcuts import render
from django.http import JsonResponse

from . import models

def home(request):
    perosona_encontrada = models.Persona.objects.first()
    proyectos_encontrados =  models.Proyecto.objects.select_related().all()
    #En caso de que la persona no existe se debe de crear una por default x)
    
    
    return render(request, 'home.html', {
        "persona" : perosona_encontrada,
        "proyectos" : proyectos_encontrados
    })

def get_curriculum(request):
    return JsonResponse({'nombre':'Felipe Garza'})