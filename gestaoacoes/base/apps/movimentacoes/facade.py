from django.contrib import messages
from django.shortcuts import render

from gestaoacoes.base.apps.movimentacoes.forms import InsereMovimentacoesForm
from gestaoacoes.base.apps.movimentacoes.models import Movimentacao
from gestaoacoes.base.apps.notas.models import Ativo


class MovimentacaoCreationExcelption(Exception):
    def __init__(self, form: InsereMovimentacoesForm, *args: object) -> None:
        super().__init__(*args)
        self.form = form

def lista_movimentacoes():
    movimentacoes = Movimentacao.objects.all().order_by('id_movimentacao')
    return movimentacoes


def criar_movimentacao(form, request):
    try:
        movimentacao = form
        movimentacao.instance.fk_ativo = movimentacao.instance.fk_ativo
        movimentacao.instance.fk_corretora = movimentacao.instance.fk_corretora
        movimentacao.instance.data_pregao = movimentacao.instance.data_pregao
        movimentacao.instance.data_liquidacao = movimentacao.instance.data_liquidacao
        movimentacao.instance.descricao = movimentacao.instance.descricao.upper()
        movimentacao.instance.tipo = movimentacao.instance.tipo.upper()
        movimentacao.instance.quantidade = movimentacao.instance.quantidade
        movimentacao.instance.valor = movimentacao.instance.valor
        try:
            movimentacao.instance.observacao = movimentacao.instance.observacao.upper()
        except:
            movimentacao.instance.observacao = movimentacao.instance.observacao

        movimentacao.save()

        # Muda o status do Ativo para "S" [Feito], o que faz com que ele não aparece no campo
        # Ativo da movimentação
        ativo_feito = Ativo.objects.get(id_ativo=movimentacao.instance.fk_ativo_id)
        ativo_feito.status ='S'
        ativo_feito.save()

        messages.success(request, 'Movimentacao "%s" criado com sucesso!' % movimentacao.instance.descricao)

    except MovimentacaoCreationExcelption as e:
        return render(request, 'movimentacoes/nova_movimentacao.html', context={'form': e.form}, status=400)
