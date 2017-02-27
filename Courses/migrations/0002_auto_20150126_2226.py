# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_type',
            field=models.CharField(max_length=8, choices=[('FULL', 'Full Day'), ('AM', 'Morning'), ('PM', 'Afternoon'), ('TRAVEL', 'Travel')], default='FULL'),
            preserve_default=True,
        ),
    ]
