import decimal

from django.contrib import messages
from django.db.models import Sum
from django.shortcuts import render

from gestaoacoes.base.apps.configuracoes.models import TipoAtivo
from gestaoacoes.base.apps.movimentacoes.forms import InsereSplitInplitForm
from gestaoacoes.base.apps.movimentacoes.models import Movimentacao
from gestaoacoes.base.apps.notas.models import Nota, Ativo, SplitInplit, NotaDaytrade, AtivoDayTrade


class SplitInplitCreationExcelption(Exception):
    def __init__(self, form: InsereSplitInplitForm, *args: object) -> None:
        super().__init__(*args)
        self.form = form


def lista_notas():
    notas = Nota.objects.all().order_by('nota')
    return notas


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
    if ativo.instance.daytrade == 'N':

        ativo.instance.fk_nota_id = nota
        ativo.instance.valor_operacao = ativo.instance.quantidade * ativo.instance.preco
        ativo.save()

        ativos = ativo.instance.fk_nota.ativo_set.all()
        messages.success(request, 'O Ativo "%s" foi inserido com sucesso.' % ativo.instance.fk_ticker)

        return ativos
    else:

        nota = Nota.objects.get(id_notas=nota)
        nota_dt = NotaDaytrade.objects.filter(nota_dt=nota.nota)

        if not nota_dt:
            nota_dt = NotaDaytrade.objects.create(
                nota_dt = nota.nota,
                fk_corretora_dt = nota.fk_corretora,
                data_pregao_dt = nota.data_pregao,
                data_liquidacao_dt = nota.data_liquidacao,
            )

        notas_dt = NotaDaytrade.objects.get(nota_dt=nota)

        ativo_dt = AtivoDayTrade.objects.create(
            fk_nota_dt_id = notas_dt.id_notas_dt ,
            status_dt = ativo.instance.status ,
            operacao_dt = ativo.instance.operacao ,
            fk_tipo_ativo_dt = ativo.instance.fk_tipo_ativo ,
            fk_ticker_dt = ativo.instance.fk_ticker ,
            quantidade_dt = ativo.instance.quantidade ,
            preco_dt = ativo.instance.preco ,
            valor_operacao_dt = ativo.instance.quantidade * ativo.instance.preco ,
        )

        messages.success(request, 'O Ativo "%s" foi inserido com sucesso.' % ativo.instance.fk_ticker)

def inserir_taxa_nota(form_2, nota, request):
    taxa = form_2

    if taxa.instance.taxa_liquidacao != 0:
        irrf = taxa.instance.irrf
        taxa_liquidacao = taxa.instance.taxa_liquidacao or 0
        taxa_registro = taxa.instance.taxa_registro or 0
        taxa_termo_opcoes = taxa.instance.taxa_termo_opcoes or 0
        taxa_ana = taxa.instance.taxa_ana or 0
        emolumentos = taxa.instance.emolumentos or 0
        taxa_operacional = taxa.instance.taxa_operacional or 0
        taxa_execucao = taxa.instance.taxa_execucao or 0
        taxa_custodia = taxa.instance.taxa_custodia or 0
        imposto = taxa.instance.imposto or 0
        outros = taxa.instance.outros or 0

        # Taxas e Reteio

        ativos = Ativo.objects.filter(fk_nota=nota)
        nota = nota

        n_ativos = Ativo.objects.filter(fk_nota=nota).count()
        n_ativos_venda = Ativo.objects.filter(fk_nota=nota, operacao="V").count()

        total_operacao = round(decimal.Decimal(
            Ativo.objects.filter(fk_nota=nota).aggregate(Sum('valor_operacao'))['valor_operacao__sum'] or 0), 2)
        total_operacao_venda = round(decimal.Decimal(
            Ativo.objects.filter(fk_nota=nota, operacao="V").aggregate(Sum('valor_operacao'))[
                'valor_operacao__sum'] or 0), 2)

        ativos_corretagem = TipoAtivo.objects.filter(corretagem__gt=0)


        for a in ativos:
            if a.operacao == "V":
                a.irrf = round((a.valor_operacao * irrf / total_operacao_venda), 2)

            elif taxa_operacional: # CORRETAGEM OU TAXA OPERACIONAL
                if a.fk_tipo_ativo in ativos_corretagem:
                    for i in ativos_corretagem:
                        if i == a.fk_tipo_ativo:
                            a.taxa_operacional = i.corretagem / n_ativos
            elif a.imposto: # IMPOSTO ISS
                pass
            else:
                a.irrf = 0.00
                a.save()

            a.taxa_liquidacao = round((a.valor_operacao * taxa_liquidacao / total_operacao), 2)
            a.taxa_registro = round((a.valor_operacao * taxa_registro / total_operacao), 2)
            a.taxa_termo_opcoes = round((a.valor_operacao * taxa_termo_opcoes / total_operacao), 2)
            a.taxa_ana = round((a.valor_operacao * taxa_ana / total_operacao), 2)
            a.emolumentos = round((a.valor_operacao * emolumentos / total_operacao), 2)
            a.taxa_execucao = round((a.valor_operacao * taxa_execucao / total_operacao), 2)
            a.taxa_custodia = round((a.valor_operacao * taxa_custodia / total_operacao), 2)
            # a.imposto = round((imposto * a.taxa_operacional / a.taxa_operacional), 2)
            a.outros = round((a.valor_operacao * outros / total_operacao), 2)
            a.taxas = a.taxa_liquidacao + a.taxa_registro + a.taxa_termo_opcoes + a.taxa_ana + a.emolumentos \
                      + a.taxa_operacional + a.taxa_execucao + a.taxa_custodia + a.imposto + a.outros
            if a.operacao == "C":
                a.valor_liquido = a.valor_operacao + a.taxas
            else:
                a.valor_liquido = a.valor_operacao - a.taxas

            a.save()

        return ativos


def edita_nota(fk_nota):
    ativo = Ativo.objects.get(id_ativo=fk_nota)
    return ativo.fk_nota


def detalhes_nota(fk_nota):
    nota = Nota.objects.get(id_notas=fk_nota)
    return nota


def detalhes_itens_pedido_fixa(fk_nota):
    nota = Nota.objects.get(id_notas=fk_nota)
    ativos = nota.ativo_set.all()
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


def deletar_nota(nota, request):
    nota = Nota.objects.get(id_notas=nota)
    nota_dt = NotaDaytrade.objects.filter(nota_dt=nota.nota)

    nota.delete()
    if nota_dt:
        nota_dt.delete()

    messages.success(request, 'A nota "%s" foi excluida com sucesso.' % nota.nota)

def deletar_ativo_detalhes(param):
    ativo = Ativo.objects.get(id_ativo=param)
    return ativo


def deletar_ativo_incluir(param):
    ativo = Ativo.objects.get(id_ativo=param)
    return ativo

############################################### NOTAS DAYTRADE ########################################################

def lista_notas_dt():
    return NotaDaytrade.objects.all().order_by('nota_dt')

def detalhes_nota_dt(fk_nota_dt):
    nota_dt = NotaDaytrade.objects.get(id_notas_dt=fk_nota_dt)
    return nota_dt

def detalhes_itens_pedido_fixa_dt(fk_nota_dt):
    nota_dt = NotaDaytrade.objects.get(id_notas_dt=fk_nota_dt)
    ativos_dt = nota_dt.ativodaytrade_set.all()
    return ativos_dt


def deletar_nota_dt(id):
    nota_dt = NotaDaytrade.objects.get(id_notas_dt=id)
    nota_dt.delete()


############################################### SPLIT INPLIT ########################################################

def lista_splits():
    splits = SplitInplit.objects.all().order_by('data_corte')
    return splits


def realizar_split_inplit(form, request):
    try:
        data = form
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
