# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AbndSite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('catastro', models.IntegerField(default=0, unique=True)),
                ('dueno', models.CharField(max_length=128)),
                ('calle', models.CharField(max_length=128)),
                ('numero', models.CharField(max_length=128)),
                ('comunidad', models.CharField(max_length=128)),
                ('cabida', models.DecimalField(max_digits=20, decimal_places=12)),
                ('tenencia', models.CharField(max_length=128)),
                ('tipo', models.CharField(max_length=128)),
                ('calificacion', models.CharField(max_length=128)),
                ('descripcion', models.CharField(max_length=128)),
                ('inundabilidad', models.CharField(max_length=128)),
                ('comentarios', models.TextField()),
                ('v_estructura', models.CharField(max_length=128)),
                ('v_solar', models.CharField(max_length=128)),
                ('v_total', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
