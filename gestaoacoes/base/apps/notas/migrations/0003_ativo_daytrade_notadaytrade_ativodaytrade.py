# Generated by Django 4.1.3 on 2022-11-19 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configuracoes', '0001_initial'),
        ('notas', '0002_ativo_irrf_dt'),
    ]

    operations = [
        migrations.AddField(
            model_name='ativo',
            name='daytrade',
            field=models.CharField(choices=[('S', 'SIM'), ('N', 'NÃO')], default='N', max_length=1, verbose_name='DayTrade'),
        ),
        migrations.CreateModel(
            name='NotaDaytrade',
            fields=[
                ('id_notas_dt', models.BigAutoField(primary_key=True, serialize=False)),
                ('nota_dt', models.CharField(db_index=True, max_length=20, unique=True, verbose_name='Nota DayTrade')),
                ('data_pregao_dt', models.DateField(verbose_name='Data Pregão DT')),
                ('data_liquidacao_dt', models.DateField(verbose_name='Data Liquidação DT')),
                ('fk_corretora_dt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracoes.corretora', verbose_name='Corretora')),
            ],
            options={
                'verbose_name_plural': 'Notas DayTrades',
            },
        ),
        migrations.CreateModel(
            name='AtivoDayTrade',
            fields=[
                ('id_ativo_dt', models.BigAutoField(primary_key=True, serialize=False)),
                ('status_dt', models.CharField(choices=[('S', 'FEITO'), ('N', 'NÃO FEITO')], default='N', max_length=1, verbose_name='status nota Dt')),
                ('operacao_dt', models.CharField(choices=[('C', 'COMPRA'), ('V', 'VENDA')], max_length=1, verbose_name='Operação Dt')),
                ('quantidade_dt', models.IntegerField(verbose_name='Quantidade Dt')),
                ('preco_dt', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Preço Dt')),
                ('valor_operacao_dt', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Valor Operação Dt')),
                ('taxas_dt', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True, verbose_name='Taxa Dt')),
                ('valor_liquido_dt', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True, verbose_name='Valor Liquido Dt')),
                ('irrf_dt', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True, verbose_name='I.R.R.F DayTrade')),
                ('taxa_liquidacao_dt', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True, verbose_name='T. Liquidação Dt')),
                ('taxa_registro_dt', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True, verbose_name='T. Registro Dt')),
                ('taxa_termo_opcoes_dt', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True, verbose_name='T. Termo Opções Dt')),
                ('taxa_ana_dt', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True, verbose_name='T. A.N.A Dt')),
                ('emolumentos_dt', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True, verbose_name='Emolumentos Dt')),
                ('taxa_operacional_dt', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True, verbose_name='Corretagem Dt')),
                ('taxa_execucao_dt', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True, verbose_name='T. Execução Dt')),
                ('taxa_custodia_dt', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True, verbose_name='T. Custódia Dt')),
                ('imposto_dt', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True, verbose_name='Imposto / ISS Dt')),
                ('outros_dt', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True, verbose_name='Outros Dt')),
                ('fk_nota_dt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notas.notadaytrade')),
                ('fk_ticker_dt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracoes.empresaslistadas', verbose_name='Ticker Dt')),
                ('fk_tipo_ativo_dt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracoes.tipoativo', verbose_name='Tipo Dt')),
            ],
            options={
                'verbose_name_plural': 'Ativos DayTrades',
            },
        ),
    ]