# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestorRestaurante', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario',
            name='unidadMedida',
            field=models.CharField(max_length=20, choices=[(b'gr', b'gramo'), (b'ml', b'mililitro'), (b'un', b'unidad'), (b'po', b'porcion')]),
        ),
    ]
