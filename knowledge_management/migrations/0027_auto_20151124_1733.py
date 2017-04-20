# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge_management', '0026_auto_20151124_1708'),
    ]

    operations = [
        migrations.RenameField(
            model_name='likecomment',
            old_name='User',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 24, 17, 33, 16, 841515)),
        ),
        migrations.AlterField(
            model_name='page',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 24, 17, 33, 16, 840514)),
        ),
    ]
