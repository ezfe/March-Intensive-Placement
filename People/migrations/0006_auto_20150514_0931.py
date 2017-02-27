# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import People.models


class Migration(migrations.Migration):

    dependencies = [
        ('People', '0005_student_should_ignore'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('instructor_id', models.CharField(unique=True, default=People.models.generateUUID, serialize=False, max_length=36, primary_key=True)),
                ('name', models.CharField(unique=True, default='', max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='student',
            unique_together=set([('first_name', 'last_name')]),
        ),
    ]
