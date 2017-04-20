# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge_management', '0048_auto_20151208_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 8, 15, 51, 20, 227858)),
        ),
        migrations.AlterField(
            model_name='document',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 8, 15, 51, 20, 228857)),
        ),
        migrations.AlterField(
            model_name='page',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 8, 15, 51, 20, 226858)),
        ),
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.CharField(max_length=50, error_messages={'required': 'This field is required', 'invalid': 'Enter a valid value'}),
        ),
    ]
