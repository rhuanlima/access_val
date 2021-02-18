import uuid # Required for unique book instances
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from django.db import models


class CicloAvaliacao(models.Model):
    dsPeriodo = models.IntegerField(
        'Período de avaliação', help_text='AAAAMM', unique=True)
    lst_acao = (
        (True, 'Ativo'),
        (False, 'Fechado'),
    )
    blStatusPerido = models.BooleanField(
        'Período Ativo?', help_text='Ativo/Fechado', default=False)

    def __str__(self):
        return str(self.dsPeriodo)

####
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

    def __str__(self):
        return self.dsUsuario

    def get_absolute_url(self):
        return reverse('acessos', args=[str(self.dsMatricula)])

    def get_profile(self):
        profile = ''
        for system in list(SystemInstance.objects.filter(dsMatricula_id=self.id)):
            profile = profile + f"sistema: {system}, "
        return profile



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

class SystemInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    dsSistema = models.ForeignKey(
        Sistema, verbose_name='Sistemas', help_text='Selecione os sistemas', on_delete=models.PROTECT, null=True)
    dsMatricula = models.ForeignKey(
        Acesso, verbose_name='Matricula', on_delete=models.PROTECT, null=True)
    dsCiclo = models.ForeignKey(
        CicloAvaliacao, verbose_name='Ciclo de avaliação', on_delete=models.PROTECT, null=True
    )
    lst_acao= (
        ('1','Manter'),
        ('0', 'Remover'),
    )
    dsStatus = models.CharField(
        'Status', max_length=1, help_text='Deseja manter o acesso ativo?', choices=lst_acao, default='1'
    )

    class Meta:
        ordering = ['dsSistema']

    def __str__(self):
    #     return f'{self.dsSistema.dsNome} ({self.dsMatricula})'

    # def get_nome_sistema(self):
        return f'{self.dsSistema.dsNome}'


