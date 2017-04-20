# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tagging_autocomplete.models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge_management', '0018_auto_20151120_0225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 20, 19, 54, 22, 776542)),
        ),
        migrations.AlterField(
            model_name='page',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 20, 19, 54, 22, 775542)),
        ),
        migrations.AlterField(
            model_name='page',
            name='tags',
            field=tagging_autocomplete.models.TagAutocompleteField(max_length=255, null=True, blank=True),
        ),
    ]
