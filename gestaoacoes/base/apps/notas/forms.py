from django import forms

from gestaoacoes.base.apps.notas.models import Nota, Ativo


class InsereNotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = '__all__'

        widgets = {'data_pregao': forms.DateInput(attrs={'data-mask': "00/00/0000"}),
                   'data_liquidacao': forms.DateInput(attrs={'data-mask': "00/00/0000"}),
                   }


class InsereAtivoForm(forms.ModelForm):
    class Meta:
        model = Ativo
        fields = ['operacao',
                  'tipo',
                  'fk_ticker',
                  'quantidade',
                  'preco',
                  'irrf',
                  'taxa_liquidacao',
                  'taxa_registro',
                  'taxa_termo_opcoes',
                  'taxa_ana',
                  'emolumentos',
                  'taxa_operacional',
                  'taxa_execucao',
                  'taxa_custodia',
                  'imposto',
                  'outros',
                  ] # '__all__'

        # widgets = {'taxas': forms.DateInput(attrs={'required': 'true'}),
        #
        #            }

