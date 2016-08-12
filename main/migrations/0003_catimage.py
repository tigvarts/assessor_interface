# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_mark_line_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatImage',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('url', models.CharField(max_length=400)),
            ],
        ),
    ]
