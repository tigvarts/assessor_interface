# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('line_no', models.IntegerField()),
                ('line_content', models.CharField(max_length=200)),
                ('line_id', models.IntegerField()),
                ('line_mark', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('text', models.TextField()),
                ('contact', models.CharField(null=True, max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='mark',
            name='query',
            field=models.ForeignKey(to='main.Query'),
        ),
    ]
