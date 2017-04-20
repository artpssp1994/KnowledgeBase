# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import tagging.fields


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge_management', '0015_auto_20151119_0136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 20, 0, 3, 24, 866767)),
        ),
        migrations.AlterField(
            model_name='page',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 20, 0, 3, 24, 865767)),
        ),
        migrations.AlterField(
            model_name='page',
            name='tags',
            field=tagging.fields.TagField(blank=True, max_length=255),
        ),
    ]
