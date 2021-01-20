# Generated by Django 3.1.5 on 2021-01-20 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acessos', '0004_systeminstance_dsmatricula'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='acesso',
            name='dsSistema',
        ),
        migrations.AddField(
            model_name='systeminstance',
            name='dsStatus',
            field=models.BooleanField(default=True, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='area',
            name='dsCoordenador',
            field=models.CharField(max_length=100, verbose_name='Nome do Coordenador'),
        ),
        migrations.AlterField(
            model_name='area',
            name='dsKeyUser',
            field=models.CharField(max_length=100, verbose_name='Nome do KeyUser'),
        ),
        migrations.AlterField(
            model_name='area',
            name='dsKeyUserEmail',
            field=models.EmailField(max_length=254),
        ),
    ]
