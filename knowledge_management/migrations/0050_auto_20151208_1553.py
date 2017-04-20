# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge_management', '0049_auto_20151208_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 8, 15, 53, 1, 515685)),
        ),
        migrations.AlterField(
            model_name='document',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 8, 15, 53, 1, 517688)),
        ),
        migrations.AlterField(
            model_name='page',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 8, 15, 53, 1, 514684)),
        ),
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.CharField(error_messages={'invalid': 'Enter a valid value', 'null': 'This field is required'}, max_length=50),
        ),
    ]
