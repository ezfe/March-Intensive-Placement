# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import Courses.models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0003_auto_20150127_1127'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.CharField(default=Courses.models.generateUUID, primary_key=True, unique=True, serialize=False, max_length=36)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('short_name', models.CharField(default=Courses.models.generateUUID, unique=True, max_length=200)),
                ('course_type', models.CharField(default='FULL', choices=[('FULL', 'Full Day'), ('AM', 'Morning'), ('PM', 'Afternoon'), ('TRAVEL', 'Travel')], max_length=8)),
                ('grade', models.IntegerField(default=9)),
                ('ford_sayre', models.CharField(choices=[('NO', 'No'), ('YES', 'Yes')], max_length=3)),
                ('hartford_tech', models.CharField(choices=[('NO', 'No'), ('AM', 'Morning'), ('PM', 'Afternoon')], max_length=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
