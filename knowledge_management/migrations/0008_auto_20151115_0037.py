# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('knowledge_management', '0007_auto_20151111_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='postby',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='page',
            name='postby',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 15, 0, 36, 59, 120757)),
        ),
        migrations.AlterField(
            model_name='page',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 15, 0, 36, 59, 119757)),
        ),
    ]
