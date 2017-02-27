# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0011_course_instructors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='instructors',
        ),
    ]
