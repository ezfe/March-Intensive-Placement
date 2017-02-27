# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0008_remove_course_short_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='is_travel',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='course_type',
            field=models.CharField(default='FULL', max_length=8, choices=[('FULL', 'Full Day'), ('AM', 'Morning'), ('PM', 'Afternoon')]),
            preserve_default=True,
        ),
    ]
