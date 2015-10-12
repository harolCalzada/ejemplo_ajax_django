from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext as ctx
from .models import Autor, Libro, Autor_Libro
from django.http import HttpResponse , JsonResponse
from django.core import serializers
# Create your views here.


def home(request):
    autores_libros = Autor_Libro.objects.all().order_by('fecha_publicacion')[:10]

    # nombres = autores[0].nombres

    # print 'nombre', nombres

    return render_to_response('home.html', locals(), context_instance=ctx(request))


def detalle_libro(request, slug):
    detalle_libro = Libro.objects.get(slug=slug)
    return render_to_response('detalle_libro.html', locals(), context_instance=ctx(request))


def busqueda_libro(request):
    if request.is_ajax():
        #logica ejemplo usuario ={'nombre': 'Eduardo Ismael'}
        # proyectos = Proyecto.objects.filter(nombre__startswith= request.GET['nombre'] ).values('nombre', 'id')
        #            return HttpResponse( json.dumps( list(proyectos)), content_type='application/json' )
        print request.GET['nombre']
        libros = Libro.objects.filter(nombre__startswith=request.GET['nombre'])
        print libros, 'libros'
        # response = JsonResponse({'nombre': libros.name})
        leads_as_json = serializers.serialize('json', libros)
        print  leads_as_json
        return HttpResponse(leads_as_json, content_type='json')
        # return HttpResponse(JsonResponse.dumps(list(libros)), content_type='aplication/json')
    else:
        return redirect('/')
#