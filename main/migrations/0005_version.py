# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20160816_0710'),
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('occured_at', models.DateTimeField(auto_now_add=True)),
                ('short_description', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
    ]
