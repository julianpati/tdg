# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='descripcion_orden',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('idOrden', models.PositiveIntegerField()),
                ('idPlato', models.CharField(max_length=20)),
                ('cantidad', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ingrediente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('plato', models.CharField(max_length=20)),
                ('ingrediente', models.CharField(max_length=20)),
                ('cantidad', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='inventario',
            fields=[
                ('idIngrediente', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=40)),
                ('unidadMedida', models.CharField(max_length=20, choices=[(b'kg', b'kilogramo'), (b'gr', b'gramo'), (b'lb', b'libra'), (b'lt', b'litro'), (b'oz', b'onza'), (b'un', b'unidad'), (b'po', b'porcion')])),
                ('cantidadDisponible', models.FloatField()),
                ('precioUnitario', models.PositiveIntegerField()),
                ('cantidadMinima', models.IntegerField()),
                ('alerta', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='menu',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('precio', models.PositiveIntegerField()),
                ('estado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='menu_platos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('menu', models.IntegerField()),
                ('plato', models.CharField(max_length=20)),
                ('tipoPlato', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='orden',
            fields=[
                ('idOrden', models.AutoField(serialize=False, primary_key=True)),
                ('mesa', models.PositiveIntegerField()),
                ('mesero', models.CharField(max_length=30)),
                ('estado', models.CharField(max_length=20, choices=[(b'FA', b'facturada'), (b'NF', b'sin_facturar')])),
            ],
        ),
        migrations.CreateModel(
            name='plato',
            fields=[
                ('idPlato', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=20)),
                ('tipo', models.CharField(max_length=20, choices=[(b'PR', b'primario'), (b'SE', b'secundario'), (b'JU', b'jugo'), (b'SO', b'soda')])),
                ('receta', models.TextField(validators=[django.core.validators.MaxLengthValidator(300)])),
                ('precio', models.PositiveIntegerField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipoUsuario', models.CharField(max_length=10, choices=[(b'R', b'Root'), (b'C', b'Chef'), (b'M', b'Mesero')])),
                ('genero', models.CharField(max_length=10, choices=[(b'M', b'Masculino'), (b'F', b'Femenino')])),
                ('tipoDocumento', models.CharField(max_length=20, choices=[(b'C.C', b'Cedula de ciudadania'), (b'T.I', b'Tarjeta de identidad')])),
                ('documento', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=50)),
                ('telefono', models.BigIntegerField()),
                ('fechaDeNacimiento', models.DateField()),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
