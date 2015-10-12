from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('apps.web.views',

    url(r'^$', 'home', name='home'),
    url(r'^detalle-libro/(?P<slug>[-\w]+)/$', 'detalle_libro', name='detalle_libro'),
    url(r'^busqueda/$', 'busqueda_libro', name='buscar_libro')
)
