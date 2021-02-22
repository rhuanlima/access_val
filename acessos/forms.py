from django.forms import ModelForm
from .models import Sistema, Acesso, Area
from django import forms


class SistemaInline(forms.ModelMultipleChoiceField):
    model = Sistema
    list_display = ('dsNome', 'dsObs')

class AcessosForm(ModelForm):
    class Meta:
        model = Acesso
        fields = ('dsMatricula', 'dsUsuario',
                  'dsUserEmail', 'dsArea', 'dsSistema')
        exclude = ('m2mthroughfield',)
    
    dsSistema = SistemaInline(
        queryset=Sistema.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

