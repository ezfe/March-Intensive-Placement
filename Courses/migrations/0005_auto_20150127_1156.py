# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0004_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='ford_sayre',
            field=models.CharField(max_length=3, default='NO', choices=[('NO', 'No'), ('YES', 'Yes')]),
            preserve_default=True,
        ),
    ]
