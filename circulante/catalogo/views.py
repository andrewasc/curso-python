# coding: utf-8

from django.http import HttpResponse
from django.shortcuts import render

import datetime
from .models import Publicacao

def home(request):
    qt_livros = Publicacao.objects.filter(tipo='livro').count()
    return render(request, 'fluid.html', {'qt_livros':qt_livros})


def listar_publicacoes(request, tipo='livro'):
    pubs = Publicacao.objects.filter(tipo=tipo).order_by('titulo')
    return render(request, 'catalogo/lista_pubs.html', {'pubs':pubs})
    
def ficha_publicacao(request, pk):
    pub = Publicacao.objects.get(pk=pk)
    return render(request, 'catalogo/ficha_pub.html', {'pub':pub})

def hora_atual(request):
    delta = int(request.GET.get('delta', 0))
    return hora_atual_delta(request, delta)


def hora_atual_delta(request, delta):
    delta = int(delta)
    delta = datetime.timedelta(hours=delta)
    hora = datetime.datetime.now()+delta
    hora = hora.strftime('%H:%M:%S')
    html = "<html><body><h1>%s</h1></body></html>" % hora
    return HttpResponse(html)
