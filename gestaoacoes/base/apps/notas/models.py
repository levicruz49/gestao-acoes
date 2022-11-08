from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from gestaoacoes.base.apps.configuracoes.models import Corretora, EmpresasListadas


# Create your models here.


class Nota(models.Model):

    id_notas = models.BigAutoField(primary_key=True)

    status = models.CharField('status nota', max_length=1, blank=True, null=True)
    nota = models.CharField('Nota', max_length=20, db_index=True)
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
    id_ativo = models.BigAutoField(primary_key=True)
    fk_nota = models.ForeignKey(Nota, on_delete=models.CASCADE)
    operacao = models.CharField('Operação', max_length=1, choices=OPERACAO)
    tipo = models.CharField('Bairro', max_length=20, choices=TIPO)
    fk_ticker = models.ForeignKey(EmpresasListadas, on_delete=models.CASCADE, verbose_name='Ticker')
    quantidade = models.IntegerField('Quantidade')
    preco = models.DecimalField('Preço', max_digits=12, decimal_places=2, default=0)
    valor_operacao = models.DecimalField('Valor Operação', max_digits=12, decimal_places=2, default=0)

    class Meta:
        verbose_name_plural = "Ativos"

    def __str__(self):
        return '{} - {}'.format(self.fk_nota.nota, self.fk_ticker)

    objects = models


class Taxa(models.Model):
    id_taxa = models.BigAutoField(primary_key=True)
    fk_ativo = models.ForeignKey(Ativo, on_delete=models.CASCADE)
    taxas = models.DecimalField('Taxa', max_digits=12, decimal_places=2, default=0)
    valor_liquido = models.DecimalField('Valor Liquido', max_digits=12, decimal_places=2, default=0)
    irrf = models.DecimalField('I.R.R.F', max_digits=12, decimal_places=2, default=0)
    taxa_liquidacao = models.DecimalField('Taxa Liquidação', max_digits=12, decimal_places=2, default=0)
    taxa_registro = models.DecimalField('Taxa Registro', max_digits=12, decimal_places=2, default=0)
    taxa_termo_opcoes = models.DecimalField('Taxa Termo Opções', max_digits=12, decimal_places=2, default=0)
    taxa_ana = models.DecimalField('Taxa A.N.A', max_digits=12, decimal_places=2, default=0)
    emolumentos = models.DecimalField('Emolumentos', max_digits=12, decimal_places=2, default=0)
    taxa_operacional = models.DecimalField('Taxa Operacional', max_digits=12, decimal_places=2, default=0)
    taxa_execucao = models.DecimalField('Taxa Execução', max_digits=12, decimal_places=2, default=0)
    taxa_custodia = models.DecimalField('Taxa Custódia', max_digits=12, decimal_places=2, default=0)
    imposto = models.DecimalField('Imposto', max_digits=12, decimal_places=2, default=0)
    outros = models.DecimalField('Outros', max_digits=12, decimal_places=2, default=0)

    class Meta:
        verbose_name_plural = "Ativos"

    def __str__(self):
        return '{} - {}'.format(self.fk_ativo.fk_ticker, self.id_taxa)

    objects = models


@receiver(post_save, sender=Ativo)
def update_vendas_total(sender, instance, **kwargs):
    instance.fk_nota.calcular_total()