from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Acesso, Area
from django.template import loader
from .forms import AcessosForm
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    acessos = Acesso.objects.all()
    return render(request, 'index.html', {'acessos': acessos})


@login_required
def acessos_list(request):
    acessos = Acesso.objects.all()
    return render(request, 'acessos_list.html', {'acessos': acessos})


@login_required
def acessos_new(request):
    form = AcessosForm(request.POST or None)
    if form.is_valid():
        list_form = form.save(commit=False)
        list_form.save()  # grava sem os itens
        form.save_m2m() # adiciona os itens
        return redirect('acessos_list')
    return render(request, 'acessos_form.html', {'form': form})


@login_required
def acessos_edit(request, id):
    acesso = get_object_or_404(Acesso, pk=id)
    form = AcessosForm(request.POST or None, instance=acesso)
    if form.is_valid():
        list_form = form.save(commit=False)
        list_form.save()  # grava sem os itens
        form.save_m2m()  # adiciona os itens
        return redirect('acessos_list')
    return render(request, 'acessos_form.html', {'form': form})


def lista_areas(request, id):
    area = get_object_or_404(Area, pk=id)
    acessos = Acesso.objects.filter(dsArea=area)
    return render(request, 'lista_areas.html', {'acessos': acessos})
