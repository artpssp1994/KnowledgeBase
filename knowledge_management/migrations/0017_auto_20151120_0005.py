# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import tagging_autocomplete.models


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge_management', '0016_auto_20151120_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 20, 0, 5, 14, 196475)),
        ),
        migrations.AlterField(
            model_name='page',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 20, 0, 5, 14, 195475)),
        ),
        migrations.AlterField(
            model_name='page',
            name='tags',
            field=tagging_autocomplete.models.TagAutocompleteField(max_length=255, blank=True),
        ),
    ]
