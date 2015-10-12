# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('dni', models.CharField(max_length=8, serialize=False, verbose_name=b'DNI', primary_key=True)),
                ('slug', models.SlugField(editable=False)),
                ('nombres', models.CharField(max_length=100, verbose_name=b'Nombres')),
                ('apellidos', models.CharField(max_length=100, verbose_name=b'Apellidos')),
                ('direccion', models.CharField(max_length=100, verbose_name=b'Direcci\xc3\xb3n')),
                ('pais', models.CharField(max_length=50, verbose_name=b'Pa\xc3\xads')),
            ],
            options={
                'ordering': ['apellidos', 'nombres'],
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
            },
        ),
        migrations.CreateModel(
            name='Autor_Libro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_publicacion', models.DateField(verbose_name=b'Fecha de publicaci\xc3\xb3n')),
                ('fk_autor', models.ForeignKey(to='web.Autor')),
            ],
            options={
                'ordering': ['fecha_publicacion'],
                'verbose_name': 'Publicaci\xf3n',
                'verbose_name_plural': 'Publicaciones',
            },
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('cod', models.CharField(max_length=20, serialize=False, verbose_name=b'C\xc3\xb3digo del libro', primary_key=True)),
                ('slug', models.SlugField(editable=False)),
                ('nombre', models.CharField(max_length=100, verbose_name=b'Nombre')),
                ('resumen', models.TextField(verbose_name=b'Resumen')),
                ('indice', models.TextField(verbose_name=b'Indice')),
                ('precio', models.DecimalField(verbose_name=b'Precio', max_digits=6, decimal_places=2)),
                ('fk_autor', models.ManyToManyField(related_name='autor_libros', verbose_name=b'Seleccionar autor(es)', through='web.Autor_Libro', to='web.Autor')),
            ],
            options={
                'ordering': ['nombre'],
                'verbose_name': 'Libro',
                'verbose_name_plural': 'Libros',
            },
        ),
        migrations.AddField(
            model_name='autor_libro',
            name='fk_libro',
            field=models.ForeignKey(to='web.Libro'),
        ),
    ]
