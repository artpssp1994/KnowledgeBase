# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=128, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=128)),
                ('data', models.TextField()),
                ('views', models.IntegerField(default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('like', models.IntegerField(default=0)),
                ('category', models.ForeignKey(to='knowledge_management.Category')),
            ],
        ),
    ]