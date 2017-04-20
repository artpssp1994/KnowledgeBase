# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('knowledge_management', '0041_auto_20151201_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='postby',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 2, 3, 36, 59, 185876)),
        ),
        migrations.AlterField(
            model_name='document',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 2, 3, 36, 59, 186876)),
        ),
        migrations.AlterField(
            model_name='page',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 2, 3, 36, 59, 184875)),
        ),
    ]
