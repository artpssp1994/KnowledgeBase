# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge_management', '0019_auto_20151120_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 21, 22, 11, 40, 178465)),
        ),
        migrations.AlterField(
            model_name='page',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 21, 22, 11, 40, 176464)),
        ),
        migrations.AlterField(
            model_name='super_category',
            name='name',
            field=models.CharField(unique=True, default='', max_length=25),
        ),
    ]
