# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0012_remove_course_instructors'),
        ('People', '0006_auto_20150514_0931'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Instructor',
        ),
    ]
