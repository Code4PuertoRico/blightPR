# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blight_app', '0004_auto_20150312_2048'),
    ]

    operations = [
        migrations.AddField(
            model_name='abndsite',
            name='lat',
            field=models.CharField(default=45, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='abndsite',
            name='lng',
            field=models.CharField(default=4546, max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='abndsite',
            name='catastro',
            field=models.CharField(max_length=128),
            preserve_default=True,
        ),
    ]
