# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.CharField(max_length=36, primary_key=True, serialize=False, unique=True)),
                ('display_name', models.CharField(max_length=200)),
                ('short_name', models.CharField(max_length=200, unique=True)),
                ('course_type', models.CharField(max_length=8, default='FULL')),
                ('max_students', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
