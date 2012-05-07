# coding: utf-8

from django.http import HttpResponse
import datetime

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
