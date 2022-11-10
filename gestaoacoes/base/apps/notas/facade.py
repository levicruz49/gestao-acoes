from django.contrib import messages

from gestaoacoes.base.apps.notas.models import Nota


def lista_notas():
    notas = Nota.objects.filter().order_by('id_notas')
    return notas

def criar_nova_nota(form, request):
    nota_criar = form

    fk_nota = Nota.objects.create(
        nota = nota_criar.instance.nota,
        fk_corretora = nota_criar.instance.fk_corretora,
        data_pregao = nota_criar.instance.data_pregao,
        data_liquidacao = nota_criar.instance.data_liquidacao,
    )

    messages.success(request,
                     'A nota "%s" criado com sucesso, agora preencha '
                     'abaixo os ativos da nota.' % nota_criar.instance.nota)
    return fk_nota

def inserir_ativo_nota(form_2, nota, request):
    ativo = form_2

    if ativo.instance.taxa_liquidacao != 0:
        ativo.instance.fk_nota_id = nota
        ativo.instance.valor_operacao = ativo.instance.quantidade * ativo.instance.preco
        ativo.save()
    else:
        ativo.instance.fk_nota_id = nota
        ativo.instance.valor_operacao = ativo.instance.quantidade * ativo.instance.preco
        ativo.save()

    ativos = ativo.instance.fk_nota.ativo_set.all()
    messages.success(request, 'O Ativo "%s" foi inserido com sucesso.' % ativo.instance.fk_ticker)

    return ativos