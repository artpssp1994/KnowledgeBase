# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge_management', '0003_auto_20151106_1952'),
    ]

    operations = [
        migrations.CreateModel(
            name='Super_category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default='', unique=True, max_length=128)),
            ],
        ),
        migrations.AlterField(
            model_name='page',
            name='date',
            field=models.TextField(default=datetime.datetime(2015, 11, 6, 19, 54, 0, 145136)),
        ),
        migrations.AddField(
            model_name='category',
            name='super_category',
            field=models.ForeignKey(to='knowledge_management.Super_category', default=''),
            preserve_default=False,
        ),
    ]
