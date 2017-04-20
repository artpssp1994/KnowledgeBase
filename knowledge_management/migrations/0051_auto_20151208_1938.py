# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge_management', '0050_auto_20151208_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='super_category',
            name='description',
            field=models.CharField(max_length=50, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 8, 19, 38, 42, 943429)),
        ),
        migrations.AlterField(
            model_name='document',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 8, 19, 38, 42, 944430)),
        ),
        migrations.AlterField(
            model_name='page',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 8, 19, 38, 42, 942428)),
        ),
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
