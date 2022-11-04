from django.db import models

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

    class Meta:
        verbose_name_plural = "Corretoras"

    def __str__(self):
        return self.nome_corretora

    objects = models