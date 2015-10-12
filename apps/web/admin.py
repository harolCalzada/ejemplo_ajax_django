from django.contrib import admin
from .models import Autor, Libro, Autor_Libro
# Register your models here.


class AutorLibroAdmin(admin.ModelAdmin):
    model = Autor_Libro
    # filter_horizontal = ('fk_libro__fk_autor',)


admin.site.register(Autor)
admin.site.register(Libro)
admin.site.register(Autor_Libro, AutorLibroAdmin)
