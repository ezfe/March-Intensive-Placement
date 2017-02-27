# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0017_auto_20151025_2020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='description',
        ),
        migrations.RemoveField(
            model_name='course',
            name='instructors',
        ),
        migrations.RemoveField(
            model_name='course',
            name='locations',
        ),
        migrations.RemoveField(
            model_name='course',
            name='readings',
        ),
    ]
