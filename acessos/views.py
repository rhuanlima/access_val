from django.shortcuts import render
from django.http import HttpResponse
from .models import Acesso
from django.template import loader


def index(request):
    acessos = Acesso.objects.order_by('dsMatricula')
    output = '<br>'.join([q.dsUsuario for q in acessos])
    return HttpResponse(len(acessos))

