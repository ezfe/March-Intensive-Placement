# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0007_delete_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='short_name',
        ),
    ]
