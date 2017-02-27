# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('People', '0006_auto_20150514_0931'),
        ('Courses', '0010_course_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='instructors',
            field=models.ManyToManyField(to='People.Instructor'),
            preserve_default=True,
        ),
    ]
