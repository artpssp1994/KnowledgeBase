# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge_management', '0005_auto_20151106_2018'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('data', models.TextField()),
                ('date', models.DateTimeField(default=datetime.datetime(2015, 11, 11, 17, 35, 38, 68991))),
                ('like', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='page',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 11, 17, 35, 38, 67990)),
        ),
        migrations.AddField(
            model_name='comment',
            name='page',
            field=models.ForeignKey(to='knowledge_management.Page'),
        ),
    ]
