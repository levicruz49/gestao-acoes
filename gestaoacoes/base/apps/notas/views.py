from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, DeleteView

from gestaoacoes.base.apps.movimentacoes.forms import InsereSplitInplitForm
from gestaoacoes.base.apps.notas import facade
from gestaoacoes.base.apps.notas.forms import InsereNotaForm, InsereAtivoForm, EditarNotaForm, EditarAtivoForm
from gestaoacoes.base.apps.notas.models import Nota


# Create your views here.

def lista_notas(request):
    # A lista de notas é pego pelo ativo... para poder pegar todos os campos de nota e ativo
    return render(request, 'notas/listar_notas.html', {'ativos': facade.lista_notas()}, )


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
                  context={'form': form, 'form2': form_2, 'fk_nota': fk_nota, 'ativos': ativos,
                           'n_nota': form.instance.nota})


def incluir_ativo_nota(request, fk_nota):

    if request.method == 'GET':
        form_2 = InsereAtivoForm()
        nota = Nota.objects.filter(id_notas=fk_nota)
        ativos = nota[0].ativo_set.all()
        return render(request, 'notas/incluir_ativo_nota.html',
                      context={'form2': form_2, 'ativos': ativos, 'fk_nota': fk_nota, 'nota': nota[0]})

    form_2 = InsereAtivoForm(request.POST)

    if not form_2.is_valid():
        return render(request, 'notas/incluir_ativo_nota.html', context={'form2': form_2})

    ativos = facade.inserir_ativo_nota_detalhes(form_2, fk_nota, request)

    # return redirect('fixa_avancada:lista_pedidos_fixa')
    return render(request, 'notas/incluir_ativo_nota.html', context={'form2': form_2, 'fk_nota': fk_nota, 'ativos': ativos,})


def nova_taxa_nota(request, fk_nota):
    obj = Nota.objects.get(id_notas=fk_nota)
    form = InsereNotaForm(instance=obj)
    form_2 = InsereAtivoForm(request.POST)

    if not form_2.is_valid():
        return render(request, 'notas/nova_nota.html', context={'form2': form_2})

    ativos = facade.inserir_taxa_nota(form_2, fk_nota, request)

    # return redirect('fixa_avancada:lista_pedidos_fixa')
    return render(request, 'notas/nova_nota.html',
                  context={'form': form, 'form2': form_2, 'fk_nota': fk_nota, 'ativos': ativos,
                           'n_nota': form.instance.nota})


class editar_nota(SuccessMessageMixin, UpdateView):
    form_class = EditarNotaForm
    template_name = 'notas/editar_nota.html'
    success_url = reverse_lazy('notas:lista_notas')
    success_message = "A nota %(nota)s, foi atualizado com sucesso!"

    def get_object(self, **kwargs):
        data = facade.edita_nota(self.kwargs['fk_nota'])
        return data


class editar_ativo(SuccessMessageMixin, UpdateView):
    form_class = EditarAtivoForm
    template_name = 'notas/editar_ativo.html'
    success_message = "O Ativo %(fk_ticker)s, foi atualizado com sucesso!"

    def get_object(self, **kwargs):
        data = facade.edita_ativo(self.kwargs['fk_nota'])
        return data

    def get_success_url(self):
        return reverse('notas:detalhes_nota', kwargs={'fk_nota': self.object.fk_nota.id_notas})


def detalhes_nota(request, fk_nota):
    return render(request, 'notas/detalhes_nota.html',
                  {'nota': facade.detalhes_nota(fk_nota),
                   'ativos': facade.detalhes_itens_pedido_fixa(fk_nota)})


def lista_split_inplit(request):
    return render(request, 'notas/listar_splitinplit.html', {'splits': facade.lista_splits()}, )


def novo_split_inplit(request):
    if request.method == 'GET':
        form = InsereSplitInplitForm()
        return render(request, 'notas/novo_split_inplit.html', context={'form': form})

    form = InsereSplitInplitForm(request.POST)
    if not form.is_valid():
        return render(request, 'notas/novo_split_inplit.html', context={'form': form})

    facade.realizar_split_inplit(form, request)

    return redirect('notas:lista_notas')


class deletar_nota(SuccessMessageMixin, DeleteView):
    template_name = 'notas/deletar_nota.html'
    success_message = 'A nota foi deletada com sucesso!'

    def get_object(self, **kwargs):
        data = facade.deletar_nota(self.kwargs['fk_nota'])
        return data

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(deletar_nota, self).delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('notas:lista_notas')


class deletar_ativo_detalhes(SuccessMessageMixin, DeleteView):
    template_name = 'notas/deletar_ativo_detalhes.html'
    success_message = 'O Ativo foi deletado com sucesso!'

    def get_object(self, **kwargs):
        data = facade.deletar_ativo_detalhes(self.kwargs['fk_nota'])
        return data

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(deletar_ativo_detalhes, self).delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('notas:detalhes_nota', kwargs={'fk_nota': self.object.fk_nota.id_notas})


class deletar_ativo_incluir(SuccessMessageMixin, DeleteView):
    template_name = 'notas/deletar_ativo_incluir.html'
    success_message = 'O Ativo foi deletado com sucesso!'

    def get_object(self, **kwargs):
        data = facade.deletar_ativo_incluir(self.kwargs['fk_nota'])
        return data

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(deletar_ativo_incluir, self).delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('notas:incluir_ativo_nota', kwargs={'fk_nota': self.object.fk_nota.id_notas})