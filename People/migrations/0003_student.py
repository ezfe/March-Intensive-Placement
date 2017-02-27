# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import People.models


class Migration(migrations.Migration):

    dependencies = [
        ('People', '0002_auto_20150127_1903'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.CharField(serialize=False, primary_key=True, unique=True, max_length=36, default=People.models.generateUUID)),
                ('grade', models.IntegerField(default=9)),
                ('ford_sayre', models.CharField(choices=[('NO', 'No'), ('YES', 'Yes')], max_length=3, default='NO')),
                ('hartford_tech', models.CharField(choices=[('NO', 'No'), ('AM', 'Morning'), ('PM', 'Afternoon')], max_length=2, default='NO')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
