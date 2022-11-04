# Generated by Django 4.1.3 on 2022-11-03 23:56

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
            ],
            options={
                'verbose_name_plural': 'Corretoras',
            },
        ),
    ]