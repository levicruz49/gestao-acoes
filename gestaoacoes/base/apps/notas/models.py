from django.db import models

# Create your models here.


# class Nota(models.Model):
#     id_notas = models.BigAutoField(primary_key=True)
#
#     incluida = models.CharField('Incluída', max_length=1)
#     nota = models.CharField('Nota', max_length=20, db_index=True)
#     corretora = models.CharField('CEP', max_length=9, null=True, blank=True)
    # Data Pregão = models.CharField('Endereço', max_length=200, null=True, blank=True)
    # Data Liquidação = models.CharField('Nº', max_length=10, null=True, blank=True)
    # C_V	 = models.CharField('Complemento', max_length=50, null=True, blank=True)
    # Tipo = models.CharField('Bairro', max_length=50)
    # Ticker = models.CharField('Estado', max_length=50)
    # Quantidade = models.CharField('Cidade', max_length=50)
    # Preço = models.CharField('Nome Responsavel', max_length=200)
    # Valor = models.CharField('CPF - Responsavel', max_length=15, blank=True, null=True)
    # Operação = models.EmailField('Email Responsavel', max_length=200)
    # Taxas = models.CharField('Cel Responsavel', max_length=14)
    # Valor = models.CharField('Tel Responsavel', max_length=14, blank=True, null=True)
    # Liquido = models.BooleanField(default=False)
    # I.R.R.F.
    # Taxa
    # Liquidação
    # Taxa
    # Registro
    # Taxa
    # Termo / Opções
    # Taxa
    # A.N.A.
    # Emolumentos
    # Taxa
    # Operacional
    # Taxa
    # Execução
    # Taxa
    # Custódia
    # Impostos
    # Outros

    # class Meta:
    #     verbose_name_plural = "Notas"
    #
    # def __str__(self):
    #     return self.nota
    #
    # objects = models