from django import forms
from django.db.models import Q

from gestaoacoes.base.apps.movimentacoes.models import Movimentacao
from gestaoacoes.base.apps.notas.models import SplitInplit, Ativo


class InsereMovimentacoesForm(forms.ModelForm):
    class Meta:
        model = Movimentacao
        fields = '__all__'

        widgets = {'data_pregao': forms.DateInput(attrs={'data-mask': "00/00/0000"}),
                   'data_liquidacao': forms.DateInput(attrs={'data-mask': "00/00/0000"}),
                   }

    def __init__(self, *args, **kwargs):
        super(InsereMovimentacoesForm, self).__init__(*args, **kwargs)

        self.fields['fk_ativo'].queryset = Ativo.objects.filter(~Q(status='S'))


class InsereSplitInplitForm(forms.ModelForm):
    class Meta:
        model = SplitInplit
        exclude = ['status', 'data_exe']
        fields = '__all__'

        widgets = {'data_corte': forms.DateInput(attrs={'data-mask': "00/00/0000"}),
                   }
        # TODO O TICKER DEVE TER APENAS OS PEPEIS QUE TENHO NA CARTEIRA
