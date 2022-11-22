from django import forms
from gestaoacoes.base.apps.configuracoes.models import Corretora, TipoAtivo


class InsereCorretoraForm(forms.ModelForm):
    class Meta:
        model = Corretora
        fields = '__all__'

        widgets = {'cnpj': forms.TextInput(attrs={'data-mask': "00.000.000/0000-00"}),
                   }


class AtualizaCorretoraForm(forms.ModelForm):
    class Meta:
        model = Corretora
        fields = '__all__'

        widgets = {'cnpj': forms.TextInput(attrs={'data-mask': "00.000.000/0000-00"}),
                   }


class InsereTipoAtivoForm(forms.ModelForm):
    class Meta:
        model = TipoAtivo
        fields = '__all__'


class AtualizaTipoAtivoForm(forms.ModelForm):
    class Meta:
        model = TipoAtivo
        fields = '__all__'