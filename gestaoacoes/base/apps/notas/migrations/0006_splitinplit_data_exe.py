# Generated by Django 4.1.3 on 2022-11-12 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0005_splitinplit_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='splitinplit',
            name='data_exe',
            field=models.DateField(auto_now=True),
        ),
    ]
