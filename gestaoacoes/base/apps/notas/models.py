from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from gestaoacoes.base.apps.configuracoes.models import Corretora, EmpresasListadas, TipoAtivo


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

    ESTATUS = (
        ('S', 'FEITO'),
        ('N', 'NÃO FEITO')
    )

    DAYTRADE = (
        ('S', 'SIM'),
        ('N', 'NÃO')
    )

    id_ativo = models.BigAutoField(primary_key=True)

    fk_nota = models.ForeignKey(Nota, on_delete=models.CASCADE)
    status = models.CharField('status nota', max_length=1, choices=ESTATUS, default='N')
    operacao = models.CharField('Operação', max_length=1, choices=OPERACAO)
    daytrade = models.CharField('DayTrade', max_length=1, choices=DAYTRADE)
    fk_tipo_ativo = models.ForeignKey(TipoAtivo, on_delete=models.CASCADE, verbose_name='Tipo')
    fk_ticker = models.ForeignKey(EmpresasListadas, on_delete=models.CASCADE, verbose_name='Ticker')
    quantidade = models.IntegerField('Quantidade')
    preco = models.DecimalField('Preço', max_digits=12, decimal_places=2, default=0)
    valor_operacao = models.DecimalField('Valor Operação', max_digits=12, decimal_places=2, default=0)
    taxas = models.DecimalField('Taxa', max_digits=12, decimal_places=2, default=0, null=True, blank=True)
    valor_liquido = models.DecimalField('Valor Liquido', max_digits=12, decimal_places=2, default=0, null=True,
                                        blank=True)
    irrf = models.DecimalField('I.R.R.F', max_digits=12, decimal_places=2, default=0, null=True, blank=True)
    taxa_liquidacao = models.DecimalField('T. Liquidação', max_digits=12, decimal_places=2, default=0, null=True,
                                          blank=True)
    taxa_registro = models.DecimalField('T. Registro', max_digits=12, decimal_places=2, default=0, null=True,
                                        blank=True)
    taxa_termo_opcoes = models.DecimalField('T. Termo Opções', max_digits=12, decimal_places=2, default=0, null=True,
                                            blank=True)
    taxa_ana = models.DecimalField('T. A.N.A', max_digits=12, decimal_places=2, default=0, null=True, blank=True)
    emolumentos = models.DecimalField('Emolumentos', max_digits=12, decimal_places=2, default=0, null=True, blank=True)
    taxa_operacional = models.DecimalField('Corretagem', max_digits=12, decimal_places=2, default=0, null=True,
                                           blank=True)
    taxa_execucao = models.DecimalField('T. Execução', max_digits=12, decimal_places=2, default=0, null=True,
                                        blank=True)
    taxa_custodia = models.DecimalField('T. Custódia', max_digits=12, decimal_places=2, default=0, null=True,
                                        blank=True)
    imposto = models.DecimalField('Imposto / ISS', max_digits=12, decimal_places=2, default=0, null=True, blank=True)
    outros = models.DecimalField('Outros', max_digits=12, decimal_places=2, default=0, null=True, blank=True)
    irrf_dt = models.DecimalField('I.R.R.F Day Trade', max_digits=12, decimal_places=2, default=0, null=True,
                                  blank=True)

    class Meta:
        verbose_name_plural = "Ativos"

    def calcular_valor_operacao(self):
        valor_operacao = self.quantidade * self.preco
        Ativo.objects.filter(id_ativo=self.id_ativo).update(valor_operacao=valor_operacao)

    def __str__(self):
        return 'ID: {} - Nota: {} - Ticker: {}'.format(self.id_ativo, self.fk_nota.nota, self.fk_ticker)

    objects = models


class NotaDaytrade(models.Model):
    id_notas_dt = models.BigAutoField(primary_key=True)

    nota_dt = models.CharField('Nota DayTrade', max_length=20, db_index=True, unique=True)
    fk_corretora_dt = models.ForeignKey(Corretora, on_delete=models.CASCADE, verbose_name='Corretora')
    data_pregao_dt = models.DateField('Data Pregão DT')
    data_liquidacao_dt = models.DateField('Data Liquidação DT')

    class Meta:
        verbose_name_plural = "Notas DayTrades"

    def __str__(self):
        return self.nota_dt

    objects = models


class AtivoDayTrade(models.Model):
    OPERACAO = (
        ('C', 'COMPRA'),
        ('V', 'VENDA'),
    )

    ESTATUS = (
        ('S', 'FEITO'),
        ('N', 'NÃO FEITO')
    )

    id_ativo_dt = models.BigAutoField(primary_key=True)

    fk_nota_dt = models.ForeignKey(NotaDaytrade, on_delete=models.CASCADE)
    status_dt = models.CharField('status nota Dt', max_length=1, choices=ESTATUS, default='N')
    operacao_dt = models.CharField('Operação Dt', max_length=1, choices=OPERACAO)
    fk_tipo_ativo_dt = models.ForeignKey(TipoAtivo, on_delete=models.CASCADE, verbose_name='Tipo Dt')
    fk_ticker_dt = models.ForeignKey(EmpresasListadas, on_delete=models.CASCADE, verbose_name='Ticker Dt')
    quantidade_dt = models.IntegerField('Quantidade Dt')
    preco_dt = models.DecimalField('Preço Dt', max_digits=12, decimal_places=2, default=0)
    valor_operacao_dt = models.DecimalField('Valor Operação Dt', max_digits=12, decimal_places=2, default=0)
    taxas_dt = models.DecimalField('Taxa Dt', max_digits=12, decimal_places=2, default=0, null=True, blank=True)
    valor_liquido_dt = models.DecimalField('Valor Liquido Dt', max_digits=12, decimal_places=2, default=0, null=True,
                                        blank=True)
    irrf_dt = models.DecimalField('I.R.R.F DayTrade', max_digits=12, decimal_places=2, default=0, null=True, blank=True)
    taxa_liquidacao_dt = models.DecimalField('T. Liquidação Dt', max_digits=12, decimal_places=2, default=0, null=True,
                                          blank=True)
    taxa_registro_dt = models.DecimalField('T. Registro Dt', max_digits=12, decimal_places=2, default=0, null=True,
                                        blank=True)
    taxa_termo_opcoes_dt = models.DecimalField('T. Termo Opções Dt', max_digits=12, decimal_places=2, default=0, null=True,
                                            blank=True)
    taxa_ana_dt = models.DecimalField('T. A.N.A Dt', max_digits=12, decimal_places=2, default=0, null=True, blank=True)
    emolumentos_dt = models.DecimalField('Emolumentos Dt', max_digits=12, decimal_places=2, default=0, null=True, blank=True)
    taxa_operacional_dt = models.DecimalField('Corretagem Dt', max_digits=12, decimal_places=2, default=0, null=True,
                                           blank=True)
    taxa_execucao_dt = models.DecimalField('T. Execução Dt', max_digits=12, decimal_places=2, default=0, null=True,
                                        blank=True)
    taxa_custodia_dt = models.DecimalField('T. Custódia Dt', max_digits=12, decimal_places=2, default=0, null=True,
                                        blank=True)
    imposto_dt = models.DecimalField('Imposto / ISS Dt', max_digits=12, decimal_places=2, default=0, null=True, blank=True)
    outros_dt = models.DecimalField('Outros Dt', max_digits=12, decimal_places=2, default=0, null=True, blank=True)


    class Meta:
        verbose_name_plural = "Ativos DayTrades"

    def calcular_valor_operacao(self):
        valor_operacao = self.quantidade_dt * self.preco_dt
        AtivoDayTrade.objects.filter(id_ativo_dt=self.id_ativo_dt).update(valor_operacao_dt=valor_operacao)

    def __str__(self):
        return 'ID: {} - Nota: {} - Ticker: {}'.format(self.id_ativo_dt, self.fk_nota_dt.nota_dt, self.fk_ticker_dt)

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


@receiver(post_save, sender=Ativo)
def update_valor_operacao(sender, instance, **kwargs):
    instance.calcular_valor_operacao()
