# Generated by Django 3.1.5 on 2021-01-20 04:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dsArea', models.CharField(max_length=100)),
                ('dsCoordenador', models.CharField(max_length=100)),
                ('dsKeyUser', models.CharField(max_length=100)),
                ('dsKeyUserEmail', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['dsArea'],
            },
        ),
        migrations.CreateModel(
            name='Sistema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dsNome', models.CharField(help_text='Insira um sistema aqui .. (ex: SAP HANA)', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Acesso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dsMatricula', models.BigIntegerField(unique=True)),
                ('dsUsuario', models.CharField(max_length=100)),
                ('dsArea', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='acessos.area')),
                ('dsSistema', models.ManyToManyField(help_text='Selecione os sistemas', to='acessos.Sistema')),
            ],
        ),
    ]
