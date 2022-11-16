# Generated by Django 4.1.3 on 2022-11-11 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configuracoes', '0005_remove_empresaslistadas_saldo_corretora_saldo'),
        ('notas', '0002_alter_ativo_taxa_ana_alter_ativo_taxa_custodia_and_more'),
        ('movimentacoes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movimentacao',
            name='fk_ativo',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='notas.ativo', verbose_name='Ativo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movimentacao',
            name='fk_corretora',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracoes.corretora', verbose_name='Corretora'),
        ),
    ]
