# Generated by Django 3.1.5 on 2021-01-20 04:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('acessos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='acesso',
            name='dtUpdate',
            field=models.DateTimeField(auto_now=True, verbose_name='Data atualização'),
        ),
        migrations.AlterField(
            model_name='acesso',
            name='dsArea',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='acessos.area', verbose_name='Area'),
        ),
        migrations.AlterField(
            model_name='acesso',
            name='dsMatricula',
            field=models.BigIntegerField(unique=True, verbose_name='Matricula'),
        ),
        migrations.AlterField(
            model_name='acesso',
            name='dsUsuario',
            field=models.CharField(max_length=100, verbose_name='Colaborador'),
        ),
        migrations.AlterField(
            model_name='area',
            name='dsArea',
            field=models.CharField(max_length=100, verbose_name='Area'),
        ),
    ]
