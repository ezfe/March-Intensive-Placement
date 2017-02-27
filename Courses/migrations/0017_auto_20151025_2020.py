# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0016_course_locations'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='manual_placement',
            field=models.BooleanField(default=False, verbose_name='manual placement'),
        ),
        migrations.AlterField(
            model_name='course',
            name='is_travel',
            field=models.BooleanField(default=False, verbose_name='travel'),
        ),
    ]
