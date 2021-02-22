import uuid # Required for unique book instances
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from django.db import models

class Sistema(models.Model):
    dsNome = models.CharField(
        max_length=100, help_text='Insira um sistema aqui .. (ex: SAP HANA)', unique = True)
    dsObs = models.CharField('Observações sobre os Acessos:', help_text='Informações sobre como cancelar o acesso', max_length=500, null=True)
    def __str__(self):
        return self.dsNome

class Acesso(models.Model):
    dsMatricula = models.BigIntegerField('Matricula', unique=True)
    dsUsuario = models.CharField('Colaborador', max_length=100)
    dsArea = models.ForeignKey(
        'Area', verbose_name='Area', on_delete=models.PROTECT, null=True)
    dsUserEmail = models.EmailField('Email', max_length=254)
    dtUpdate = models.DateTimeField(verbose_name = 'Última alteração',auto_now=True)
    dsSistema = models.ManyToManyField(Sistema, verbose_name='Acessos Ativos', blank=True)

    def __str__(self):
        return self.dsUsuario

    def get_access(self):
        return "\n".join([p.dsNome for p in self.dsSistema.all()])

    def get_access_html(self):
        return list(self.dsSistema.all())
        #return len(self.dsSistema.all())

    def get_absolute_url(self):
        return reverse('acessos', args=[str(self.dsMatricula)])


class Area(models.Model):
    """Model representing an author."""
    dsArea = models.CharField('Area',max_length=100)
    dsCoordenador = models.CharField('Nome do Coordenador', max_length=100)
    dsKeyUser = models.CharField('Nome do KeyUser', max_length=100)
    dsKeyUserEmail = models.EmailField(max_length=254)
    class Meta:
        ordering = ['dsArea']

    def get_absolute_url(self):
        return reverse('area', args=[str(self.id)])

    def __str__(self):
        return f'{self.dsArea}'


