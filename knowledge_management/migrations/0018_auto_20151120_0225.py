# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge_management', '0017_auto_20151120_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 20, 2, 25, 29, 281196)),
        ),
        migrations.AlterField(
            model_name='page',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 20, 2, 25, 29, 280196)),
        ),
    ]
