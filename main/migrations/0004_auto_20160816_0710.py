# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_catimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='mark',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 8, 16, 7, 10, 16, 835635, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='query',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 8, 16, 7, 10, 33, 590851, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
