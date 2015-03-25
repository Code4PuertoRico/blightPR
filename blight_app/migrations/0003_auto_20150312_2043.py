# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blight_app', '0002_auto_20150312_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abndsite',
            name='cabida',
            field=models.CharField(max_length=128),
            preserve_default=True,
        ),
    ]
