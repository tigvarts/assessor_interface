# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_version'),
    ]

    operations = [
        migrations.AddField(
            model_name='mark',
            name='version',
            field=models.ForeignKey(to='main.Version', null=True),
        ),
        migrations.AddField(
            model_name='query',
            name='version',
            field=models.ForeignKey(to='main.Version', null=True),
        ),
    ]
