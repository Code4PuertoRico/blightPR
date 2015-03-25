# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blight_app', '0003_auto_20150312_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abndsite',
            name='catastro',
            field=models.CharField(unique=True, max_length=128),
            preserve_default=True,
        ),
    ]
