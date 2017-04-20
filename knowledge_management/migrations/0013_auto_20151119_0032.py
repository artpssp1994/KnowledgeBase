# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tagging_autocomplete.models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge_management', '0012_auto_20151118_2356'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='tags',
            field=tagging_autocomplete.models.TagAutocompleteField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 19, 0, 32, 59, 378199)),
        ),
        migrations.AlterField(
            model_name='page',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 19, 0, 32, 59, 377199)),
        ),
    ]
