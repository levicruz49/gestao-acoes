from django.shortcuts import render

from gestaoacoes.base.apps.notas import facade


# Create your views here.

def lista_notas(request):
    return render(request, 'notas/listar_notas.html',)
