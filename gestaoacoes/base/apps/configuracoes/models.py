from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


class Corretora(models.Model):
    ATIVA = (
        ('S', 'SIM'),
        ('N', 'NÃO'),
    )
    id_corretoras = models.BigAutoField(primary_key=True)

    nome_corretora = models.CharField('Nome', max_length=200, db_index=True)
    razao_social = models.CharField('Razão Social', max_length=200)
    cnpj = models.CharField('Nº CNPJ', max_length=18)
    ativa = models.CharField('Ativa', max_length=1, choices=ATIVA)
    saldo = models.DecimalField('Saldo', max_digits=12, decimal_places=2, default=0)


    class Meta:
        verbose_name_plural = "Corretoras"

    def __str__(self):
        return self.nome_corretora

    objects = models


class EmpresasListadas(models.Model):
    id_empresas_listadas = models.BigAutoField(primary_key=True)
    ticker = models.CharField('Ticker', max_length=30)
    cnpj = models.CharField('Nº CNPJ', max_length=18, blank=True, null=True)
    razao_social = models.CharField('Razão Social', max_length=200)

    class Meta:
        verbose_name_plural = "Empresas Listadas"

    def __str__(self):
        return self.ticker

    objects = models


class TipoAtivo(models.Model):
    id_tipo_ativo = models.BigAutoField(primary_key=True)

    nome_tipo_ativo = models.CharField('Nome Ativo', max_length=200)
    corretagem = models.DecimalField('Corretagem', max_digits=12, decimal_places=2, default=0)

    class Meta:
        verbose_name_plural = "Tipos Ativos"

    def __str__(self):
        return self.nome_tipo_ativo

    objects = models
