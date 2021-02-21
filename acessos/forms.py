from django.forms import ModelForm
from .models import Sistema, Acesso, Area, SystemInstance, CicloAvaliacao



class SystemInstanceInline(ModelForm):
    model = SystemInstance
    list_display = ('dsSistema', 'dsObs', 'dsStatus')
    verbose_name = "Acesso"
    verbose_name_plural = "Meus acessos"

class AcessosForm(ModelForm):
    class Meta:
        model = Acesso
        fields = ('dsMatricula', 'dsUsuario', 'dsUserEmail', 'dsArea')
    
        inlines = [SystemInstanceInline]
