from django.http import HttpResponse
from AppCoder.models import Curso
from django.shortcuts import render


# Create your views here.
def curso(self):
    curso = Curso(nombre='Desarrollo Web', camada='19881')
    curso.save()

    documentoDeTexto = f'---->Curso: {curso.nombre} Camada:{curso.camada}'

    return HttpResponse(documentoDeTexto)