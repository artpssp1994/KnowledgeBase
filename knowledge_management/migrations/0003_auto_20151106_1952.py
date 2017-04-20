# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge_management', '0002_auto_20151106_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='date',
            field=models.TextField(default=datetime.datetime(2015, 11, 6, 19, 52, 0, 666169)),
        ),
    ]
