from django import forms
from gestaoacoes.base.apps.configuracoes.models import Corretora


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
