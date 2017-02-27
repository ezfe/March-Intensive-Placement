# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import Courses.models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0002_auto_20150126_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_id',
            field=models.CharField(default=Courses.models.generateUUID, primary_key=True, serialize=False, unique=True, max_length=36),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='short_name',
            field=models.CharField(default=Courses.models.generateUUID, unique=True, max_length=200),
            preserve_default=True,
        ),
    ]
