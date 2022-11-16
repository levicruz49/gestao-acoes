from django.shortcuts import render, redirect

from gestaoacoes.base.apps.movimentacoes import facade
from gestaoacoes.base.apps.movimentacoes.forms import InsereMovimentacoesForm


# Create your views here.

def lista_movimentacoes(request):
    return render(request, 'movimentacoes/listar_movimentacoes.html', {'movimentacoes': facade.lista_movimentacoes()}, )


def nova_movimentacao(request):
    if request.method == 'GET':
        form = InsereMovimentacoesForm()
        return render(request, 'movimentacoes/nova_movimentacao.html', context={'form': form})

    form = InsereMovimentacoesForm(request.POST)
    if not form.is_valid():
        return render(request, 'movimentacoes/nova_movimentacao.html', context={'form': form})

    facade.criar_movimentacao(form, request)

    return redirect('movimentacoes:lista_movimentacoes')