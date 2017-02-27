# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0005_auto_20150127_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='hartford_tech',
            field=models.CharField(max_length=2, choices=[('NO', 'No'), ('AM', 'Morning'), ('PM', 'Afternoon')], default='NO'),
            preserve_default=True,
        ),
    ]
