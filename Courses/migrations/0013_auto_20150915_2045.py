# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0012_remove_course_instructors'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.CharField(max_length=200, default='No Description'),
        ),
        migrations.AddField(
            model_name='course',
            name='instructors',
            field=models.CharField(max_length=3000, default='No Instructors'),
        ),
    ]
