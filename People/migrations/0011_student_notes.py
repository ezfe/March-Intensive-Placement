# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('People', '0010_student_student_leader'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='notes',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
