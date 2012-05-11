from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^pubs/$', 'catalogo.views.listar_publicacoes'),
    url(r'^pub/(\d+)$', 'catalogo.views.ficha_publicacao'),
    url(r'^hora/$', 'catalogo.views.hora_atual', name='hora'),
    url(r'^hora/(-?\d\d?)$', 'catalogo.views.hora_atual_delta', name='hora-caminho'),
)

