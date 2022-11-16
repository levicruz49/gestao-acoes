from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from gestaoacoes.base.apps.configuracoes.models import Corretora
from gestaoacoes.base.apps.notas.models import Ativo


# Create your models here.

class Movimentacao(models.Model):
    id_movimentacao = models.BigAutoField(primary_key=True)
    fk_corretora = models.ForeignKey(Corretora, on_delete=models.CASCADE, verbose_name='Corretora')
    fk_ativo = models.ForeignKey(Ativo, on_delete=models.CASCADE, verbose_name='Ativo', blank=True, null=True)
    data_pregao = models.DateField('Data Pregão')
    data_liquidacao = models.DateField('Data Liquidação')
    descricao = models.CharField('Descrição', max_length=200)
    tipo = models.CharField('Tipo', max_length=200)
    quantidade = models.IntegerField('Quantidade', blank=True, null=True)
    valor = models.DecimalField('Valor', max_digits=12, decimal_places=2, default=0, null=True,
                                        blank=True)
    observacao = models.CharField('Observação', max_length=200, blank=True, null=True)


    def calcular_saldo(self):
        pass

    class Meta:
        verbose_name_plural = 'Movimentações'

    def __str__(self):
        return '{} - {}'.format(self.id_movimentacao, self.descricao)

    objects = models


@receiver(post_save, sender=Movimentacao)
def update_saldo_movimentacao(sender, instance, **kwargs):
    instance.calcular_saldo()