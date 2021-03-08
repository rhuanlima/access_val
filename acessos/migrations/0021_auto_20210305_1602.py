# Generated by Django 3.1.5 on 2021-03-05 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acessos', '0020_auto_20210305_1445'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rede',
            name='dsNome',
        ),
        migrations.AlterField(
            model_name='acesso',
            name='dsRede',
            field=models.ManyToManyField(blank=True, to='acessos.Rede', verbose_name='Pastas de Rede'),
        ),
        migrations.AlterField(
            model_name='acesso',
            name='dsSistema',
            field=models.ManyToManyField(blank=True, to='acessos.Sistema', verbose_name='Sistemas Internos'),
        ),
        migrations.AlterField(
            model_name='acesso',
            name='dsSistemaExterno',
            field=models.ManyToManyField(blank=True, to='acessos.SistemaExterno', verbose_name='Sistemas Externos'),
        ),
        migrations.AlterField(
            model_name='acesso',
            name='dsUserWeb',
            field=models.CharField(max_length=100, unique=True, verbose_name='Usuário de Rede'),
        ),
        migrations.AlterField(
            model_name='rede',
            name='dsCaminho',
            field=models.CharField(help_text='Insira o caminho completo', max_length=100, unique=True, verbose_name='Caminho da Pasta:'),
        ),
        migrations.AlterField(
            model_name='rede',
            name='dsObs',
            field=models.CharField(help_text='Informações sobre como cancelar/solicitar o acesso', max_length=500, null=True, verbose_name='Observações sobre os diretório:'),
        ),
        migrations.AlterField(
            model_name='sistema',
            name='dsNome',
            field=models.CharField(help_text='Insira um sistema aqui .. (ex: SAP HANA)', max_length=100, unique=True, verbose_name='Nome do Sistema:'),
        ),
        migrations.AlterField(
            model_name='sistemaexterno',
            name='dsNome',
            field=models.CharField(help_text='Insira um sistema aqui .. (ex: SAP HANA)', max_length=100, unique=True, verbose_name='Nome do Sistema Exteno:'),
        ),
    ]
