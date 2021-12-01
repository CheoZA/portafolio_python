from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.utils.encoding import smart_str
from django.contrib.staticfiles.views import serve

from . import models
from . import documentos


def home(request):
    perosona_encontrada = models.Persona.objects.first()
    proyectos_encontrados =  models.Proyecto.objects.select_related().all()
    
    #En caso de que la persona no existe se debe de crear una por default x)
    '''if perosona_encontrada is None:
        persona_nueva = models.Persona()
        persona_nueva.nombre = "nombre"
        persona_nueva.apellido = "apellido"
        persona_nueva.fecha_de_nacimiento = DateTime()
        models.Persona.objects.create(Persona())
    '''
        
    return render(request, 'home.html', {
        "persona" : perosona_encontrada,
        "proyectos" : proyectos_encontrados
    })

def get_curriculum(request):
    documentos.curriculum.generar_cv()
    return serve(request, '/generated/cv.pdf')