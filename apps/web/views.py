import json
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext as ctx
from .models import Autor, Libro, Autor_Libro
from django.http import  JsonResponse
from django.core import serializers

def home(request):
    autores_libros = Autor_Libro.objects.all().order_by('fecha_publicacion')[:10]

    return render_to_response('home.html', locals(), context_instance=ctx(request))


def detalle_libro(request, slug):
    detalle_libro = Libro.objects.get(slug=slug)
    return render_to_response('detalle_libro.html', locals(), context_instance=ctx(request))


def busqueda_libro(request):

    if request.is_ajax() and request.method == 'GET':
        libros = Libro.objects.filter(nombre__startswith=request.GET['nombre'])
        libro_json = serializers.serialize('json', libros)
        libro_json = json.loads(libro_json)
        return JsonResponse(libro_json, safe=False)
    else:
        return redirect('/')
#