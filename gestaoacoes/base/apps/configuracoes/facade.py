from django.contrib import messages
from django.shortcuts import render
from unicodedata import normalize
from gestaoacoes.base.apps.configuracoes.forms import InsereCorretoraForm, AtualizaCorretoraForm
from gestaoacoes.base.apps.configuracoes.models import Corretora


class CorretoraCreationExcelption(Exception):
    def __init__(self, form: InsereCorretoraForm, *args: object) -> None:
        super().__init__(*args)
        self.form = form

class CorretoraEditiExcelption(Exception):
    def __init__(self, form: AtualizaCorretoraForm, *args: object) -> None:
        super().__init__(*args)
        self.form = form

def listar_corretora():
    corretoras = Corretora.objects.filter(ativa='S').order_by('nome_corretora')
    return corretoras


def criar_corretora(form, request):
    try:
        corretora = form
        corretora.instance.nome_corretora = corretora.instance.nome_corretora.upper()
        corretora.instance.razao_social = corretora.instance.razao_social.upper()
        corretora.instance.cnpj = removerCaracteresEspeciais(corretora.instance.cnpj)
        corretora.instance.saldo = corretora.instance.saldo

        corretora.save()
        messages.success(request, 'Corretora "%s" criado com sucesso!' % corretora.instance.nome_corretora)

    except CorretoraCreationExcelption as e:
        return render(request, 'configuracoes/nova_corretora.html', context={'form': e.form}, status=400)

def edita_corretora(form, request):
    try:
        corretora = form
        corretora.instance.nome_corretora = corretora.instance.nome_corretora.upper()
        corretora.instance.razao_social = corretora.instance.razao_social.upper()
        corretora.instance.cnpj = removerCaracteresEspeciais(corretora.instance.cnpj)
        corretora.instance.saldo = corretora.instance.saldo

        corretora.save()

    except CorretoraEditiExcelption as e:
        return render(request, 'configuracoes/editar_corretora.html', context={'form': e.form}, status=400)


def atualiza_corretora(pk):
    aut_corretora = Corretora.objects.get(id_corretoras=pk)
    return aut_corretora


def deletar_corretora(pk):
    del_corretora = Corretora.objects.get(id_corretoras=pk)
    return del_corretora


def removerCaracteresEspeciais(text):
    if text is not None:
        text = text.replace('-', '').replace('.', '').replace('/', '').replace('(', '').replace(')', '').replace(
            '  ',
            ' ')
        return normalize('NFKD', text).encode('ASCII', 'ignore').decode('ASCII')
