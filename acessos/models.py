import uuid # Required for unique book instances
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from django.db import models


class Sistema(models.Model):
    dsNome = models.CharField(
        max_length=100, help_text='Insira um sistema aqui .. (ex: SAP HANA)')

    def __str__(self):
        return self.dsNome


class Acesso(models.Model):
    dsMatricula = models.BigIntegerField('Matricula', unique=True)
    dsUsuario = models.CharField('Colaborador', max_length=100)
    dsArea = models.ForeignKey(
        'Area',verbose_name='Area', on_delete=models.SET_NULL, null=True)

    # dsSistema = models.ManyToManyField(
    #     Sistema, verbose_name='Sistemas', help_text='Selecione os sistemas')
    
    dtUpdate = models.DateTimeField(verbose_name = 'Última alteração',auto_now=True)

    def __str__(self):
        return self.dsUsuario

    def get_absolute_url(self):
        return reverse('acessos', args=[str(self.dsMatricula)])


class SystemInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    dsSistema = models.ForeignKey(
        Sistema, verbose_name='Sistemas', help_text='Selecione os sistemas', on_delete=models.SET_NULL, null=True)
    dsMatricula = models.ForeignKey(
        Acesso, verbose_name='Matricula', on_delete=models.SET_NULL, null=True)
    dsStatus = models.BooleanField(
        'Status', help_text='Deseja manter o acesso ativo?', default=True)
    class Meta:
        ordering = ['dsSistema']

    def __str__(self):
        return f'{self.dsSistema.dsNome} ({self.dsMatricula})'


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
