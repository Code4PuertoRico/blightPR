# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blight_app', '0006_auto_20150318_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abndsite',
            name='comentarios',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
