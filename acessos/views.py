from django.shortcuts import render
from django.http import HttpResponse
from .models import Acesso
from django.template import loader
from .forms import AcessosForm

def index(request):
    acessos = Acesso.objects.order_by('dsMatricula')
    output = '<br>'.join([q.dsUsuario for q in acessos])
    return render(request, 'index.html', {'acessos': acessos})

def acessos_list(request):
    pass


def acessos_new(request):
    form = AcessosForm(request.POST, None)
    return render(request, 'acessos_form.html', {'form':form})


def acessos_edit(request):
    pass
