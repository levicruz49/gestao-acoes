from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from gestaoacoes.base.apps.configuracoes.models import Corretora, EmpresasListadas


# Create your models here.


class Nota(models.Model):

    id_notas = models.BigAutoField(primary_key=True)

    nota = models.CharField('Nota', max_length=20, db_index=True, unique=True)
    fk_corretora = models.ForeignKey(Corretora, on_delete=models.CASCADE, verbose_name='Corretora')
    data_pregao = models.DateField('Data Pregão')
    data_liquidacao = models.DateField('Data Liquidação')


    class Meta:
        verbose_name_plural = "Notas"


    def __str__(self):
        return self.nota

    objects = models


class Ativo(models.Model):
    OPERACAO = (
        ('C', 'COMPRA'),
        ('V', 'VENDA'),
    )
    TIPO = (
        ('ACAO', 'AÇÃO'),
        ('ETF', 'ETF'),
        ('FII', 'FII'),
        ('BDR', 'BDR'),
        ('OPCAO', 'OPÇÃO'),
        ('FUTURO', 'FUTURO'),
        ('STOCK', 'STOCK'),
        ('REIT', 'REIT'),
        ('PREV.PRI', 'PREVIDENCIA PRIVADA'),
    )
    ESTATUS = (
        ('S', 'FEITO'),
        ('N', 'NÃO FEITO')
    )

    id_ativo = models.BigAutoField(primary_key=True)

    fk_nota = models.ForeignKey(Nota, on_delete=models.CASCADE)
    status = models.CharField('status nota', max_length=1, choices=ESTATUS, default='N')
    operacao = models.CharField('Operação', max_length=1, choices=OPERACAO)
    tipo = models.CharField('Tipo', max_length=20, choices=TIPO)
    fk_ticker = models.ForeignKey(EmpresasListadas, on_delete=models.CASCADE, verbose_name='Ticker')
    quantidade = models.IntegerField('Quantidade')
    preco = models.DecimalField('Preço', max_digits=12, decimal_places=2, default=0)
    valor_operacao = models.DecimalField('Valor Operação', max_digits=12, decimal_places=2, default=0)
    taxas = models.DecimalField('Taxa', max_digits=12, decimal_places=2, default=0, null=True, blank=True)
    valor_liquido = models.DecimalField('Valor Liquido', max_digits=12, decimal_places=2, default=0, null=True, blank=True)
    irrf = models.DecimalField('I.R.R.F', max_digits=12, decimal_places=2, default=0, null=True, blank=True)
    taxa_liquidacao = models.DecimalField('T. Liquidação', max_digits=12, decimal_places=2, default=0, null=True, blank=True)
    taxa_registro = models.DecimalField('T. Registro', max_digits=12, decimal_places=2, default=0, null=True, blank=True)
    taxa_termo_opcoes = models.DecimalField('T. Termo Opções', max_digits=12, decimal_places=2, default=0, null=True, blank=True)
    taxa_ana = models.DecimalField('T. A.N.A', max_digits=12, decimal_places=2, default=0, null=True, blank=True)
    emolumentos = models.DecimalField('Emolumentos', max_digits=12, decimal_places=2, default=0, null=True, blank=True)
    taxa_operacional = models.DecimalField('T. Operacional', max_digits=12, decimal_places=2, default=0, null=True, blank=True)
    taxa_execucao = models.DecimalField('T. Execução', max_digits=12, decimal_places=2, default=0, null=True, blank=True)
    taxa_custodia = models.DecimalField('T. Custódia', max_digits=12, decimal_places=2, default=0, null=True, blank=True)
    imposto = models.DecimalField('Imposto', max_digits=12, decimal_places=2, default=0, null=True, blank=True)
    outros = models.DecimalField('Outros', max_digits=12, decimal_places=2, default=0, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Ativos"

    def __str__(self):
        return 'ID: {} - Nota: {} - Ticker: {}'.format(self.id_ativo, self.fk_nota.nota, self.fk_ticker)

    objects = models


class SplitInplit(models.Model):
    ESTATUS = (
        ('S', 'FEITO'),
        ('N', 'NÃO FEITO')
    )

    id_splitinplit = models.BigAutoField(primary_key=True)
    fk_ticker = models.ForeignKey(EmpresasListadas, on_delete=models.CASCADE, verbose_name='Ticker')
    proporcao_de = models.IntegerField('Proporção DE')
    proporcao_para = models.IntegerField('Proporção PARA')
    data_corte = models.DateField()
    status = models.CharField('Status', max_length=1, choices=ESTATUS, default='N')
    data_exe = models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = "Splits Inplits"

    def __str__(self):
        return 'Ticker: {} - De: {} - Para: {}'.format(self.fk_ticker.ticker, self.proporcao_de, self.proporcao_para)

    objects = models