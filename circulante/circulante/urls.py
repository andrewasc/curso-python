from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^hora/$', 'catalogo.views.hora_atual', name='hora-atual'),
    url(r'^hora/(-?\d\d?)$', 'catalogo.views.hora_atual_delta', name='hora_atual_delta'),
    # url(r'^circulante/', include('circulante.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
