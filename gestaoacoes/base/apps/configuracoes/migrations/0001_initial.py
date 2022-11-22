# Generated by Django 4.1.3 on 2022-11-18 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Corretora',
            fields=[
                ('id_corretoras', models.BigAutoField(primary_key=True, serialize=False)),
                ('nome_corretora', models.CharField(db_index=True, max_length=200, verbose_name='Nome')),
                ('razao_social', models.CharField(max_length=200, verbose_name='Razão Social')),
                ('cnpj', models.CharField(max_length=18, verbose_name='Nº CNPJ')),
                ('ativa', models.CharField(choices=[('S', 'SIM'), ('N', 'NÃO')], max_length=1, verbose_name='Ativa')),
                ('saldo', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Saldo')),
            ],
            options={
                'verbose_name_plural': 'Corretoras',
            },
        ),
        migrations.CreateModel(
            name='EmpresasListadas',
            fields=[
                ('id_empresas_listadas', models.BigAutoField(primary_key=True, serialize=False)),
                ('ticker', models.CharField(max_length=30, verbose_name='Ticker')),
                ('cnpj', models.CharField(blank=True, max_length=18, null=True, verbose_name='Nº CNPJ')),
                ('razao_social', models.CharField(max_length=200, verbose_name='Razão Social')),
            ],
            options={
                'verbose_name_plural': 'Empresas Listadas',
            },
        ),
        migrations.CreateModel(
            name='TipoAtivo',
            fields=[
                ('id_tipo_ativo', models.BigAutoField(primary_key=True, serialize=False)),
                ('nome_tipo_ativo', models.CharField(max_length=200, verbose_name='Nome Ativo')),
                ('corretagem', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Corretagem')),
            ],
            options={
                'verbose_name_plural': 'Tipos Ativos',
            },
        ),
    ]
