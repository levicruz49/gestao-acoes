from django.shortcuts import render

from gestaoacoes.base.apps.notas import facade
from gestaoacoes.base.apps.notas.forms import InsereNotaForm, InsereAtivoForm
from gestaoacoes.base.apps.notas.models import Nota


# Create your views here.

def lista_notas(request):
    return render(request, 'notas/listar_notas.html', {'notas': facade.lista_notas()}, )

def nova_nota(request):

    if request.method == 'GET':
        form = InsereNotaForm()

        return render(request, 'notas/nova_nota.html', context={'form': form})

    form = InsereNotaForm(request.POST)
    form_2 = InsereAtivoForm(request.POST)

    if not form.is_valid():
        return render(request, 'notas/nova_nota.html', context={'form': form})

    fk_nota = facade.criar_nova_nota(form, request)

    # return redirect('fixa_avancada:lista_pedidos_fixa')s
    return render(request, 'notas/nova_nota.html',
                  context={'form': form, 'form2': form_2, 'fk_nota': fk_nota.pk, 'n_nota': fk_nota.nota})

def novo_ativo_nota(request, fk_nota):

    obj = Nota.objects.get(id_notas=fk_nota)
    form = InsereNotaForm(instance=obj)
    form_2 = InsereAtivoForm(request.POST)

    if not form_2.is_valid():
        return render(request, 'notas/nova_nota.html', context={'form2': form_2})

    ativos = facade.inserir_ativo_nota(form_2, fk_nota, request)

    # return redirect('fixa_avancada:lista_pedidos_fixa')
    return render(request, 'notas/nova_nota.html',
                  context={'form': form, 'form2': form_2, 'fk_nota': fk_nota, 'ativos': ativos, 'n_nota': form.instance.nota})

def incluir_ativo_nova(request):
    pass

def novo_taxa_nota(request):
    pass