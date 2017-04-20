# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='date',
            field=models.TextField(default=0),
        ),
    ]
