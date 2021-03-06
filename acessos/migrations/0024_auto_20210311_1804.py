# Generated by Django 3.1.5 on 2021-03-11 21:04

import acessos.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acessos', '0023_remove_acesso_coteste'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sistema',
            name='dsNome',
            field=acessos.models.UpperCaseCharField(help_text='Insira um sistema aqui .. (ex: SAP HANA)', max_length=100, unique=True, verbose_name='Nome do Sistema:'),
        ),
        migrations.AlterField(
            model_name='sistemaexterno',
            name='dsNome',
            field=acessos.models.UpperCaseCharField(help_text='Insira um sistema aqui .. (ex: SAP HANA)', max_length=100, unique=True, verbose_name='Nome do Sistema Exteno:'),
        ),
    ]
