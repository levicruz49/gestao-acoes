from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView

from gestaoacoes.base.apps.configuracoes import facade
from gestaoacoes.base.apps.configuracoes.facade import criar_corretora, edita_corretora
from gestaoacoes.base.apps.configuracoes.forms import InsereCorretoraForm, AtualizaCorretoraForm, InsereTipoAtivoForm, \
    AtualizaTipoAtivoForm


# Create your views here.


def lista_corretoras(request):
    return render(request, 'configuracoes/listar_corretoras.html', {'corretoras': facade.listar_corretora(), })


def nova_corretora(request):
    if request.method == 'GET':
        form = InsereCorretoraForm()
        return render(request, 'configuracoes/nova_corretora.html', context={'form': form})

    form = InsereCorretoraForm(request.POST)
    if not form.is_valid():
        return render(request, 'configuracoes/nova_corretora.html', context={'form': form})

    facade.criar_corretora(form, request)

    return redirect('configuracoes:lista_corretoras')


class editar_corretora(SuccessMessageMixin, UpdateView):
    form_class = AtualizaCorretoraForm
    template_name = 'configuracoes/editar_corretora.html'
    success_url = reverse_lazy('configuracoes:lista_corretoras')
    success_message = 'Corretora "%(nome_corretora)s" Foi atualizado com sucesso!'

    def get_object(self, **kwargs):
        data = facade.atualiza_corretora(self.kwargs['pk'])
        return data


class deletar_corretora(DeleteView):
    template_name = 'configuracoes/deletar_corretora.html'
    success_url = reverse_lazy('configuracoes:lista_corretoras')
    success_message = 'Corretora "%(nome_corretora)s" Foi deletado com sucesso!'

    def get_object(self, **kwargs):
        data = facade.deletar_corretora(self.kwargs['pk'])
        return data

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(deletar_corretora, self).delete(request, *args, **kwargs)


def listar_tipos_ativo(request):
    return render(request, 'configuracoes/listar_tipo_ativo.html', {'tipos': facade.listar_tipos_ativos()}, )


def novo_tipo_ativo(request):
    if request.method == 'GET':
        form = InsereTipoAtivoForm()
        return render(request, 'configuracoes/novo_tipo_ativo.html', context={'form': form})

    form = InsereTipoAtivoForm(request.POST)
    if not form.is_valid():
        return render(request, 'configuracoes/novo_tipo_ativo.html', context={'form': form})

    facade.criar_tipo_ativo(form, request)

    return redirect('configuracoes:listar_tipos_ativo')


class editar_tipo_ativo(SuccessMessageMixin, UpdateView):
    form_class = AtualizaTipoAtivoForm
    template_name = 'configuracoes/editar_tipo_ativo.html'
    success_url = reverse_lazy('configuracoes:listar_tipos_ativo')
    success_message = 'Ativo "%(nome_tipo_ativo)s" Foi atualizado com sucesso!'

    def get_object(self, **kwargs):
        data = facade.atualiza_tipo_ativo(self.kwargs['pk'])
        return data


class deletar_tipo_ativo(DeleteView):
    template_name = 'configuracoes/deletar_tipo_ativo.html'
    success_url = reverse_lazy('configuracoes:listar_tipos_ativo')
    success_message = 'Ativo "%(nome_tipo_ativo)s" Foi deletado com sucesso!'

    def get_object(self, **kwargs):
        data = facade.deletar_tipo_ativo(self.kwargs['pk'])
        return data

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(deletar_tipo_ativo, self).delete(request, *args, **kwargs)
