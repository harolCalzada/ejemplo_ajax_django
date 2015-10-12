# -*- coding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.


class Autor (models.Model):
    dni = models.CharField('DNI', max_length=8, primary_key=True)
    slug = models.SlugField(editable=False)
    nombres = models.CharField('Nombres', max_length=100)
    apellidos = models.CharField('Apellidos', max_length=100)
    direccion = models.CharField('Dirección',  max_length=100)
    pais = models.CharField('País', max_length=50)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre_completo)
        super(Autor, self).save(*args, **kwargs)

    def nombre_completo(self):
        return u'%s, %s' % (self.apellidos, self.nombres)

    def __str__(self):
        return u'%s, %s' % (self.apellidos, self.nombres)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['apellidos', 'nombres']


class Libro(models.Model):
    fk_autor = models.ManyToManyField(Autor, through='Autor_Libro', related_name='autor_libros', verbose_name='Seleccionar autor(es)')
    cod = models.CharField('Código del libro', max_length=20,  primary_key=True)
    slug = models.SlugField(editable=False)
    nombre = models.CharField('Nombre', max_length=100)
    resumen = models.TextField('Resumen')
    indice = models.TextField('Indice')
    precio = models.DecimalField('Precio', max_digits=6,  decimal_places=2)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super(Libro, self).save(*args, **kwargs)

    # def obtener_autores(self, cod):
    #     return self.fk_autor_get.all()

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['nombre']


class Autor_Libro(models.Model):
    fk_autor = models.ForeignKey(Autor)
    fk_libro = models.ForeignKey(Libro)
    fecha_publicacion = models.DateField('Fecha de publicación')

    def __str__(self):
        return u'%s-%s' % (self.fk_autor.nombre_completo, self.fk_libro.nombre)

    # def agregar_autores(self):
    #     return self.fk_libro.fk_autor
    # def obtener_autores(self):
    #     ##aka no se como implementar este metodo
    #     return self.libro_set.all()

    class Meta:
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones'
        ordering = ['fecha_publicacion']

