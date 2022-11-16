from django.contrib import messages
from django.shortcuts import render

from gestaoacoes.base.apps.movimentacoes.forms import InsereSplitInplitForm
from gestaoacoes.base.apps.movimentacoes.models import Movimentacao
from gestaoacoes.base.apps.notas.models import Nota, Ativo, SplitInplit


class SplitInplitCreationExcelption(Exception):
    def __init__(self, form: InsereSplitInplitForm, *args: object) -> None:
        super().__init__(*args)
        self.form = form


def lista_notas():
    ativos = Ativo.objects.all().order_by('-fk_nota__nota')
    return ativos


def criar_nova_nota(form, request):
    nota_criar = form

    fk_nota = Nota.objects.create(
        nota=nota_criar.instance.nota,
        fk_corretora=nota_criar.instance.fk_corretora,
        data_pregao=nota_criar.instance.data_pregao,
        data_liquidacao=nota_criar.instance.data_liquidacao,
    )

    messages.success(request,
                     'A nota "%s" criado com sucesso, agora preencha '
                     'abaixo os ativos da nota.' % nota_criar.instance.nota)
    return fk_nota


def inserir_ativo_nota(form_2, nota, request):
    ativo = form_2

    ativo.instance.fk_nota_id = nota
    ativo.instance.valor_operacao = ativo.instance.quantidade * ativo.instance.preco
    ativo.save()


    ativos = ativo.instance.fk_nota.ativo_set.all()
    messages.success(request, 'O Ativo "%s" foi inserido com sucesso.' % ativo.instance.fk_ticker)

    return ativos


def inserir_taxa_nota(form_2, nota, request):
    taxa = form_2

    if taxa.instance.taxa_liquidacao != 0:

        irrf = taxa.instance.irrf
        taxa_liquidacao = taxa.instance.taxa_liquidacao
        taxa_registro = taxa.instance.taxa_registro
        taxa_termo_opcoes = taxa.instance.taxa_termo_opcoes
        taxa_ana = taxa.instance.taxa_ana
        emolumentos = taxa.instance.emolumentos
        taxa_operacional = taxa.instance.taxa_operacional
        taxa_execucao = taxa.instance.taxa_execucao
        taxa_custodia = taxa.instance.taxa_custodia
        imposto = taxa.instance.imposto
        outros = taxa.instance.outros

        taxas = None
        valor_liquido = None

def lista_splits():
    splits = SplitInplit.objects.all().order_by('data_corte')
    return splits


def realizar_split_inplit(form, request):
    try:
        data = form
        if data.instance.proporcao_de < data.instance.proporcao_para:
            # SPLIT
            data.instance.fk_ticker = data.instance.fk_ticker
            data.instance.proporcao_de = data.instance.proporcao_de
            data.instance.proporcao_para = data.instance.proporcao_para
            data.instance.data_corte = data.instance.data_corte
            data.instance.status = 'S'
            data.save()

            # Faz o SPLIT Notas
            ativos_nt = Ativo.objects.filter(fk_ticker=data.instance.fk_ticker,
                                             fk_nota__data_pregao__lte=data.instance.data_corte)

            # Faz o SPLIT nas MOVIMENTAÇÕES
            ativos_mv = Movimentacao.objects.filter(descricao=data.instance.fk_ticker,
                                                    data_pregao__lte=data.instance.data_corte)
            # LOOP NOTAS
            for ativo in ativos_nt:
                # QTD
                ativo.quantidade = int(ativo.quantidade * data.instance.proporcao_para / data.instance.proporcao_de)
                # VALOR
                ativo.preco = ativo.preco * data.instance.proporcao_de / data.instance.proporcao_para

                ativo.save()

            # LOOP MOVIMENTAÇÕES
            for movimentacao in ativos_mv:
                movimentacao.quantidade = int(
                    movimentacao.quantidade * data.instance.proporcao_para / data.instance.proporcao_de)

                movimentacao.save()





    except SplitInplitCreationExcelption as e:
        return render(request, 'notas/novo_split_inplit.html', context={'form': e.form}, status=400)


def edita_nota(fk_nota):
    ativo = Ativo.objects.get(id_ativo=fk_nota)
    return ativo.fk_nota


def detalhes_nota(fk_nota):
    nota = Ativo.objects.get(id_ativo=fk_nota)
    return nota.fk_nota


def detalhes_itens_pedido_fixa(fk_nota):
    nota = Ativo.objects.get(id_ativo=fk_nota)
    ativos = nota.fk_nota.ativo_set.all()
    return ativos


def edita_ativo(param):
    ativo = Ativo.objects.get(id_ativo=param)
    return ativo


def inserir_ativo_nota_detalhes(form_2, fk_ativo, request):
    ativo = form_2

    ativo.instance.fk_nota_id = fk_ativo
    ativo.instance.valor_operacao = ativo.instance.quantidade * ativo.instance.preco
    ativo.save()

    ativos = ativo.instance.fk_nota.ativo_set.all()
    messages.success(request, 'O Ativo "%s" foi inserido com sucesso.' % ativo.instance.fk_ticker)

    return ativos


def deletar_nota(param):
    nota = Nota.objects.get(id_notas=param)
    return nota


def deletar_ativo_detalhes(param):
    ativo = Ativo.objects.get(id_ativo=param)
    return ativo


def deletar_ativo_incluir(param):
    ativo = Ativo.objects.get(id_ativo=param)
    return ativo